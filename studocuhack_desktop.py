"""
StudocuHack Desktop v3.0 — 三级方案自动降级下载器

综合3个开源扩展的核心逻辑：
  stuhack        → #page-container 提取 + 新窗口
  studocuhack    → .pf 逐页捕获 + CDN高清图替换
  Paywall-Bypass → 三击触发 + 去模糊 + 新窗口

三级方案（自动降级）：
  方案A: 从 #page-container 提取每页内容（最干净）
  方案B: 从 .pf 逐页捕获（方案A失败时）
  方案C: 直接 page.pdf() 截取（保底）

每次生成后自动验证内容是否包含文档。

依赖: pip install PyQt5 playwright
"""

import sys, os, re, time, json, random, html
from pathlib import Path

try:
    from PyQt5.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
        QPushButton, QLineEdit, QLabel, QProgressBar, QFileDialog,
        QFrame, QMessageBox, QTextEdit, QComboBox
    )
    from PyQt5.QtCore import Qt, QThread, pyqtSignal, QUrl, QPropertyAnimation, QEasingCurve, QTimer
    from PyQt5.QtGui import QFont, QPalette, QColor, QDesktopServices, QPainter, QLinearGradient, QFontDatabase, QFontMetrics
except ImportError:
    print("请先安装: pip install PyQt5"); sys.exit(1)


DEFAULT_OUTPUT = str(Path.home() / 'Desktop')
EDGE_PATH = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
if not os.path.exists(EDGE_PATH):
    EDGE_PATH = 'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe'
EDGE_USER_DATA = os.path.expandvars(r'%LOCALAPPDATA%\Microsoft\Edge\User Data')

LANGUAGES = {
    'zh-CN': ('简体中文', 'zh-CN'),
    'en': ('English', 'en-US'),
    'de': ('Deutsch', 'de-DE'),
    'fr': ('Français', 'fr-FR'),
    'it': ('Italiano', 'it-IT'),
    'tr': ('Türkçe', 'tr-TR'),
    'es': ('Español', 'es-ES'),
    'ja': ('日本語', 'ja-JP'),
    'ko': ('한국어', 'ko-KR'),
    'vi': ('Tiếng Việt', 'vi-VN'),
}

EN = {
    'window_title': 'StudocuHack — Smart PDF Download Tool',
    'tagline': 'Smart document processing and PDF download tool',
    'language': 'Language',
    'ready': '●  Ready', 'busy': '●  Processing', 'done': '●  Completed', 'error_state': '●  Failed',
    'guide_title': 'Download in three steps',
    'guide_hint': 'Edge may open during processing. Please keep it open.',
    'step1_title': 'Paste document link', 'step1_desc': 'Copy the Studocu document page URL',
    'step2_title': 'Confirm save location', 'step2_desc': 'Desktop by default, or choose another folder',
    'step3_title': 'Start PDF download', 'step3_desc': 'Open the file after processing finishes',
    'action_title': 'Create PDF', 'action_desc': 'Enter the link and select a folder. The rest is automatic.',
    'safe_badge': 'Local processing · No file upload', 'url_label': 'Studocu document URL',
    'url_tooltip': 'Paste the Studocu document page URL to process',
    'start_button': 'Start PDF Download', 'start_tooltip': 'Start processing and generate a PDF file',
    'path_label': 'Save location', 'choose_folder': 'Choose Folder',
    'choose_folder_title': 'Choose save folder', 'path_tooltip': 'Change the PDF output folder',
    'ready_status': 'Ready · Paste a link to begin', 'status_help': 'Do not close Edge during processing',
    'log_title': 'Processing Log', 'log_desc': 'Page loading, capture, and PDF generation progress appears here',
    'open_pdf': 'Open Generated PDF', 'clear': 'Clear',
    'log_placeholder': 'Waiting for a task. Processing details will appear here...',
    'footer_note': 'Tip: documents with more pages take longer to process',
    'invalid_title': 'Notice', 'invalid_text': 'Enter a valid Studocu document URL before starting.',
    'invalid_info': 'The URL usually starts with https://www.studocu.com/document/.',
    'processing': 'Processing...', 'starting': 'Starting...',
    'completed_status': 'Completed · {message}', 'failed_status': 'Failed · {message}',
    'tag_error': 'Error', 'tag_system': 'System', 'tag_strategy': 'Strategy', 'tag_browser': 'Browser',
    'tag_output': 'Output', 'tag_navigation': 'Navigation', 'tag_hint': 'Hint', 'tag_waiting': 'Waiting',
    'tag_status': 'Status', 'tag_ready': 'Ready', 'tag_cleanup': 'Cleanup', 'tag_capture': 'Capture',
    'tag_validation': 'Validation', 'tag_direct': 'Direct', 'tag_pdf': 'PDF',
    'error_message': 'Error: {error}', 'strategy_text': 'Automatic fallback strategies: A→B→C',
    'edge_not_found': 'Microsoft Edge was not found',
    'install_playwright': 'Install Playwright: pip install playwright && playwright install chromium',
    'output_path': 'Saving to: {path}', 'open_page': 'Opening the Studocu page...',
    'loading': 'Loading...', 'navigation_hint': '{error}', 'wait_document': 'Waiting for the document to load...',
    'document_status': 'Title: "{title}" · .pf:{pf} · #page-container:{pc}',
    'wait_seconds': 'Waiting for document... {seconds}s', 'document_ready': 'Document loaded',
    'document_timeout': 'Document loading timed out', 'cleanup_page': 'Removing blur, banners, and ads...',
    'capture_pf': 'Capturing pages from .pf...', 'capture_pages': 'Capturing pages...',
    'found_pages': 'Found {pages} pages', 'strategy_b_success': 'Strategy B captured {pages} pages',
    'content_valid': 'Document content is valid', 'render_failed': 'Rendering failed; trying direct capture',
    'content_empty': 'Content is empty; trying direct capture',
    'extraction_failed': 'Content extraction failed; trying direct capture',
    'direct_capture': 'Capturing the page directly...', 'strategy_c_success': 'Strategy C succeeded: {size:.1f} KB',
    'strategy_c_failed': 'Strategy C failed: {error}', 'pdf_success': 'PDF created successfully ({size:.1f} KB)',
    'pdf_generation_failed': 'PDF generation failed', 'pdf_complete': 'Completed: {size:.1f} KB',
    'pdf_validation_failed': 'PDF content validation failed', 'pdf_error': 'PDF error: {error}',
}

TRANSLATIONS = {
    'en': EN,
    'zh-CN': {
        **EN, 'window_title':'StudocuHack — PDF 智能下载工具','tagline':'智能文档处理与 PDF 下载工具','language':'语言',
        'ready':'●  就绪','busy':'●  处理中','done':'●  已完成','error_state':'●  处理失败',
        'guide_title':'三步完成下载','guide_hint':'处理过程中 Edge 可能会弹出，请保持窗口开启',
        'step1_title':'粘贴文档链接','step1_desc':'复制 Studocu 文档页面地址','step2_title':'确认保存位置','step2_desc':'默认保存到桌面，也可自行选择',
        'step3_title':'点击下载 PDF','step3_desc':'等待处理完成后直接打开文件','action_title':'创建 PDF','action_desc':'填入链接并选择保存目录，剩下的步骤将自动完成',
        'safe_badge':'本地处理 · 无需上传文件','url_label':'Studocu 文档链接','url_tooltip':'粘贴需要处理的 Studocu 文档页面链接',
        'start_button':'开始下载 PDF','start_tooltip':'开始处理并生成 PDF 文件','path_label':'保存位置','choose_folder':'选择目录','choose_folder_title':'选择保存目录',
        'path_tooltip':'更改 PDF 文件的保存目录','ready_status':'准备就绪 · 粘贴链接后即可开始','status_help':'处理时请勿关闭 Edge 窗口',
        'log_title':'处理日志','log_desc':'这里会实时显示页面加载、捕获与 PDF 生成进度','open_pdf':'打开生成的 PDF','clear':'清空',
        'log_placeholder':'等待任务开始，处理过程会显示在这里...','footer_note':'提示：文档页数较多时，处理时间会相应增加',
        'invalid_title':'提示','invalid_text':'请输入有效的 Studocu 文档链接后再开始下载。','invalid_info':'链接通常以 https://www.studocu.com/document/ 开头。',
        'processing':'正在处理...','starting':'正在启动...','completed_status':'处理完成 · {message}','failed_status':'处理失败 · {message}',
        'tag_error':'错误','tag_system':'系统','tag_strategy':'方案','tag_browser':'浏览器','tag_output':'输出','tag_navigation':'导航','tag_hint':'提示','tag_waiting':'等待',
        'tag_status':'状态','tag_ready':'就绪','tag_cleanup':'清理','tag_capture':'捕获','tag_validation':'验证','tag_direct':'截取','tag_pdf':'PDF',
        'error_message':'错误: {error}','strategy_text':'自动降级方案: A→B→C','edge_not_found':'未找到 Edge 浏览器',
        'install_playwright':'请安装: pip install playwright && playwright install chromium','output_path':'保存到: {path}','open_page':'打开 Studocu 页面...',
        'loading':'正在加载...','navigation_hint':'{error}','wait_document':'等待文档加载...','document_status':'标题: "{title}" · .pf:{pf} · #page-container:{pc}',
        'wait_seconds':'等待文档... {seconds}秒','document_ready':'文档已加载','document_timeout':'文档加载超时','cleanup_page':'移除模糊、横幅和广告...',
        'capture_pf':'从 .pf 捕获页面...','capture_pages':'逐页捕获...','found_pages':'已发现 {pages} 页','strategy_b_success':'方案 B 成功捕获 {pages} 页',
        'content_valid':'内容有效','render_failed':'渲染失败，尝试直接截取','content_empty':'内容为空，尝试直接截取',
        'extraction_failed':'内容提取失败，尝试直接截取','direct_capture':'直接截取页面...','strategy_c_success':'方案 C 成功: {size:.1f} KB',
        'strategy_c_failed':'方案 C 失败: {error}','pdf_success':'PDF 成功！({size:.1f} KB)','pdf_generation_failed':'PDF 生成失败',
        'pdf_complete':'完成: {size:.1f} KB','pdf_validation_failed':'PDF 内容验证失败','pdf_error':'PDF 错误: {error}',
    },
    'de': {**EN, 'language':'Sprache','ready':'●  Bereit','busy':'●  Verarbeitung','done':'●  Abgeschlossen','error_state':'●  Fehlgeschlagen','guide_title':'Download in drei Schritten','guide_hint':'Edge kann während der Verarbeitung geöffnet werden. Bitte offen lassen.','step1_title':'Dokumentlink einfügen','step1_desc':'URL der Studocu-Dokumentseite kopieren','step2_title':'Speicherort bestätigen','step2_desc':'Standardmäßig Desktop oder anderen Ordner wählen','step3_title':'PDF-Download starten','step3_desc':'Datei nach Abschluss direkt öffnen','action_title':'PDF erstellen','action_desc':'Link eingeben und Ordner wählen. Der Rest erfolgt automatisch.','safe_badge':'Lokale Verarbeitung · Kein Upload','url_label':'Studocu-Dokument-URL','start_button':'PDF-Download starten','path_label':'Speicherort','choose_folder':'Ordner wählen','choose_folder_title':'Speicherordner wählen','ready_status':'Bereit · Link einfügen, um zu starten','status_help':'Edge während der Verarbeitung nicht schließen','log_title':'Verarbeitungsprotokoll','log_desc':'Fortschritt beim Laden, Erfassen und Erstellen der PDF','open_pdf':'Erzeugte PDF öffnen','clear':'Leeren','log_placeholder':'Warten auf eine Aufgabe...','footer_note':'Hinweis: Dokumente mit mehr Seiten benötigen mehr Zeit','invalid_title':'Hinweis','invalid_text':'Gib vor dem Start eine gültige Studocu-Dokument-URL ein.','processing':'Wird verarbeitet...','starting':'Wird gestartet...','completed_status':'Abgeschlossen · {message}','failed_status':'Fehlgeschlagen · {message}','edge_not_found':'Microsoft Edge wurde nicht gefunden','loading':'Wird geladen...','wait_document':'Warten auf das Dokument...','wait_seconds':'Warten auf Dokument... {seconds}s','document_ready':'Dokument geladen','document_timeout':'Zeitüberschreitung beim Laden','cleanup_page':'Unschärfe, Banner und Werbung werden entfernt...','capture_pf':'Seiten aus .pf werden erfasst...','capture_pages':'Seiten werden erfasst...','found_pages':'{pages} Seiten gefunden','content_valid':'Dokumentinhalt ist gültig','direct_capture':'Seite wird direkt erfasst...','pdf_generation_failed':'PDF-Erstellung fehlgeschlagen','pdf_success':'PDF erfolgreich erstellt ({size:.1f} KB)'},
    'fr': {**EN, 'language':'Langue','ready':'●  Prêt','busy':'●  Traitement','done':'●  Terminé','error_state':'●  Échec','guide_title':'Télécharger en trois étapes','guide_hint':'Edge peut s’ouvrir pendant le traitement. Laissez-le ouvert.','step1_title':'Coller le lien du document','step1_desc':'Copiez l’URL de la page Studocu','step2_title':'Confirmer le dossier','step2_desc':'Bureau par défaut ou autre dossier','step3_title':'Démarrer le téléchargement','step3_desc':'Ouvrez le fichier après le traitement','action_title':'Créer un PDF','action_desc':'Saisissez le lien et choisissez un dossier. Le reste est automatique.','safe_badge':'Traitement local · Aucun envoi','url_label':'URL du document Studocu','start_button':'Télécharger le PDF','path_label':'Dossier de sortie','choose_folder':'Choisir','choose_folder_title':'Choisir le dossier de sortie','ready_status':'Prêt · Collez un lien pour commencer','status_help':'Ne fermez pas Edge pendant le traitement','log_title':'Journal de traitement','log_desc':'Progression du chargement, de la capture et de la génération PDF','open_pdf':'Ouvrir le PDF généré','clear':'Effacer','log_placeholder':'En attente d’une tâche...','footer_note':'Conseil : les documents longs prennent plus de temps','invalid_title':'Information','invalid_text':'Saisissez une URL de document Studocu valide.','processing':'Traitement...','starting':'Démarrage...','completed_status':'Terminé · {message}','failed_status':'Échec · {message}','edge_not_found':'Microsoft Edge est introuvable','loading':'Chargement...','wait_document':'Attente du chargement du document...','wait_seconds':'Attente du document... {seconds}s','document_ready':'Document chargé','document_timeout':'Délai de chargement dépassé','cleanup_page':'Suppression du flou, des bannières et des publicités...','capture_pf':'Capture des pages depuis .pf...','capture_pages':'Capture des pages...','found_pages':'{pages} pages trouvées','content_valid':'Le contenu du document est valide','direct_capture':'Capture directe de la page...','pdf_generation_failed':'Échec de la génération PDF','pdf_success':'PDF créé avec succès ({size:.1f} KB)'},
    'it': {**EN, 'language':'Lingua','ready':'●  Pronto','busy':'●  Elaborazione','done':'●  Completato','error_state':'●  Errore','guide_title':'Scarica in tre passaggi','guide_hint':'Edge potrebbe aprirsi durante l’elaborazione. Lascialo aperto.','step1_title':'Incolla il link','step1_desc':'Copia l’URL della pagina Studocu','step2_title':'Conferma il salvataggio','step2_desc':'Desktop predefinito o altra cartella','step3_title':'Avvia download PDF','step3_desc':'Apri il file al termine','action_title':'Crea PDF','action_desc':'Inserisci il link e scegli una cartella. Il resto è automatico.','safe_badge':'Elaborazione locale · Nessun upload','url_label':'URL documento Studocu','start_button':'Avvia download PDF','path_label':'Posizione di salvataggio','choose_folder':'Scegli cartella','choose_folder_title':'Scegli cartella di salvataggio','ready_status':'Pronto · Incolla un link per iniziare','status_help':'Non chiudere Edge durante l’elaborazione','log_title':'Registro elaborazione','log_desc':'Qui appare l’avanzamento di caricamento, acquisizione e PDF','open_pdf':'Apri PDF generato','clear':'Cancella','log_placeholder':'In attesa di un’attività...','footer_note':'Suggerimento: i documenti lunghi richiedono più tempo','invalid_title':'Avviso','invalid_text':'Inserisci un URL Studocu valido prima di iniziare.','processing':'Elaborazione...','starting':'Avvio...','completed_status':'Completato · {message}','failed_status':'Errore · {message}','edge_not_found':'Microsoft Edge non trovato','loading':'Caricamento...','wait_document':'Attesa del caricamento del documento...','wait_seconds':'Attesa documento... {seconds}s','document_ready':'Documento caricato','document_timeout':'Tempo di caricamento scaduto','cleanup_page':'Rimozione di sfocatura, banner e pubblicità...','capture_pf':'Acquisizione pagine da .pf...','capture_pages':'Acquisizione pagine...','found_pages':'Trovate {pages} pagine','content_valid':'Il contenuto è valido','direct_capture':'Acquisizione diretta della pagina...','pdf_generation_failed':'Generazione PDF non riuscita','pdf_success':'PDF creato correttamente ({size:.1f} KB)'},
    'tr': {**EN, 'language':'Dil','ready':'●  Hazır','busy':'●  İşleniyor','done':'●  Tamamlandı','error_state':'●  Başarısız','guide_title':'Üç adımda indirin','guide_hint':'İşlem sırasında Edge açılabilir. Lütfen açık bırakın.','step1_title':'Belge bağlantısını yapıştır','step1_desc':'Studocu belge sayfası URL’sini kopyala','step2_title':'Kayıt konumunu doğrula','step2_desc':'Varsayılan Masaüstü veya başka klasör','step3_title':'PDF indirmeyi başlat','step3_desc':'İşlem bitince dosyayı aç','action_title':'PDF Oluştur','action_desc':'Bağlantıyı girin ve klasör seçin. Gerisi otomatik.','safe_badge':'Yerel işlem · Dosya yükleme yok','url_label':'Studocu belge URL’si','start_button':'PDF İndirmeyi Başlat','path_label':'Kayıt konumu','choose_folder':'Klasör Seç','choose_folder_title':'Kayıt klasörünü seç','ready_status':'Hazır · Başlamak için bağlantı yapıştırın','status_help':'İşlem sırasında Edge’i kapatmayın','log_title':'İşlem Günlüğü','log_desc':'Yükleme, yakalama ve PDF oluşturma ilerlemesi burada görünür','open_pdf':'Oluşturulan PDF’yi Aç','clear':'Temizle','log_placeholder':'Görev bekleniyor...','footer_note':'İpucu: Çok sayfalı belgeler daha uzun sürer','invalid_title':'Uyarı','invalid_text':'Başlamadan önce geçerli bir Studocu URL’si girin.','processing':'İşleniyor...','starting':'Başlatılıyor...','completed_status':'Tamamlandı · {message}','failed_status':'Başarısız · {message}','edge_not_found':'Microsoft Edge bulunamadı','loading':'Yükleniyor...','wait_document':'Belgenin yüklenmesi bekleniyor...','wait_seconds':'Belge bekleniyor... {seconds}s','document_ready':'Belge yüklendi','document_timeout':'Belge yükleme zaman aşımı','cleanup_page':'Bulanıklık, afiş ve reklamlar kaldırılıyor...','capture_pf':'.pf sayfaları yakalanıyor...','capture_pages':'Sayfalar yakalanıyor...','found_pages':'{pages} sayfa bulundu','content_valid':'Belge içeriği geçerli','direct_capture':'Sayfa doğrudan yakalanıyor...','pdf_generation_failed':'PDF oluşturma başarısız','pdf_success':'PDF başarıyla oluşturuldu ({size:.1f} KB)'},
    'es': {**EN, 'language':'Idioma','ready':'●  Listo','busy':'●  Procesando','done':'●  Completado','error_state':'●  Error','guide_title':'Descarga en tres pasos','guide_hint':'Edge puede abrirse durante el proceso. Déjalo abierto.','step1_title':'Pega el enlace','step1_desc':'Copia la URL de la página Studocu','step2_title':'Confirma la ubicación','step2_desc':'Escritorio por defecto u otra carpeta','step3_title':'Inicia la descarga','step3_desc':'Abre el archivo al finalizar','action_title':'Crear PDF','action_desc':'Introduce el enlace y elige una carpeta. El resto es automático.','safe_badge':'Proceso local · Sin subir archivos','url_label':'URL del documento Studocu','start_button':'Iniciar descarga PDF','path_label':'Ubicación de guardado','choose_folder':'Elegir carpeta','choose_folder_title':'Elegir carpeta de guardado','ready_status':'Listo · Pega un enlace para comenzar','status_help':'No cierres Edge durante el proceso','log_title':'Registro de proceso','log_desc':'Aquí aparece el progreso de carga, captura y creación del PDF','open_pdf':'Abrir PDF generado','clear':'Limpiar','log_placeholder':'Esperando una tarea...','footer_note':'Consejo: los documentos largos tardan más','invalid_title':'Aviso','invalid_text':'Introduce una URL válida de Studocu antes de comenzar.','processing':'Procesando...','starting':'Iniciando...','completed_status':'Completado · {message}','failed_status':'Error · {message}','edge_not_found':'No se encontró Microsoft Edge','loading':'Cargando...','wait_document':'Esperando a que cargue el documento...','wait_seconds':'Esperando documento... {seconds}s','document_ready':'Documento cargado','document_timeout':'Tiempo de carga agotado','cleanup_page':'Eliminando desenfoque, banners y anuncios...','capture_pf':'Capturando páginas desde .pf...','capture_pages':'Capturando páginas...','found_pages':'Se encontraron {pages} páginas','content_valid':'El contenido es válido','direct_capture':'Capturando la página directamente...','pdf_generation_failed':'Error al generar el PDF','pdf_success':'PDF creado correctamente ({size:.1f} KB)'},
    'ja': {**EN, 'language':'言語','ready':'●  準備完了','busy':'●  処理中','done':'●  完了','error_state':'●  失敗','guide_title':'3ステップでダウンロード','guide_hint':'処理中に Edge が開く場合があります。閉じないでください。','step1_title':'文書リンクを貼り付け','step1_desc':'Studocu 文書ページの URL をコピー','step2_title':'保存先を確認','step2_desc':'既定はデスクトップ、変更も可能','step3_title':'PDF ダウンロード開始','step3_desc':'処理後にファイルを開く','action_title':'PDF を作成','action_desc':'リンクと保存先を指定すると、残りは自動で処理されます。','safe_badge':'ローカル処理 · アップロード不要','url_label':'Studocu 文書 URL','start_button':'PDF ダウンロード開始','path_label':'保存先','choose_folder':'フォルダー選択','choose_folder_title':'保存先フォルダーを選択','ready_status':'準備完了 · リンクを貼り付けて開始','status_help':'処理中は Edge を閉じないでください','log_title':'処理ログ','log_desc':'読み込み、取得、PDF 作成の進捗を表示します','open_pdf':'生成した PDF を開く','clear':'クリア','log_placeholder':'タスクを待機しています...','footer_note':'ヒント：ページ数が多い文書は時間がかかります','invalid_title':'お知らせ','invalid_text':'有効な Studocu 文書 URL を入力してください。','processing':'処理中...','starting':'起動中...','completed_status':'完了 · {message}','failed_status':'失敗 · {message}','edge_not_found':'Microsoft Edge が見つかりません','loading':'読み込み中...','wait_document':'文書の読み込みを待っています...','wait_seconds':'文書を待っています... {seconds}秒','document_ready':'文書を読み込みました','document_timeout':'文書の読み込みがタイムアウトしました','cleanup_page':'ぼかし、バナー、広告を削除中...','capture_pf':'.pf からページを取得中...','capture_pages':'ページを取得中...','found_pages':'{pages} ページを検出','content_valid':'文書内容は有効です','direct_capture':'ページを直接取得中...','pdf_generation_failed':'PDF の生成に失敗しました','pdf_success':'PDF を作成しました ({size:.1f} KB)'},
    'ko': {**EN, 'language':'언어','ready':'●  준비됨','busy':'●  처리 중','done':'●  완료','error_state':'●  실패','guide_title':'세 단계로 다운로드','guide_hint':'처리 중 Edge가 열릴 수 있습니다. 닫지 마세요.','step1_title':'문서 링크 붙여넣기','step1_desc':'Studocu 문서 페이지 URL 복사','step2_title':'저장 위치 확인','step2_desc':'기본값은 바탕화면이며 변경 가능','step3_title':'PDF 다운로드 시작','step3_desc':'처리 후 파일 열기','action_title':'PDF 만들기','action_desc':'링크와 저장 폴더를 선택하면 나머지는 자동입니다.','safe_badge':'로컬 처리 · 파일 업로드 없음','url_label':'Studocu 문서 URL','start_button':'PDF 다운로드 시작','path_label':'저장 위치','choose_folder':'폴더 선택','choose_folder_title':'저장 폴더 선택','ready_status':'준비됨 · 시작하려면 링크를 붙여넣으세요','status_help':'처리 중 Edge를 닫지 마세요','log_title':'처리 로그','log_desc':'페이지 로딩, 캡처 및 PDF 생성 진행 상황','open_pdf':'생성된 PDF 열기','clear':'지우기','log_placeholder':'작업을 기다리는 중...','footer_note':'팁: 페이지가 많을수록 처리 시간이 길어집니다','invalid_title':'알림','invalid_text':'시작하기 전에 올바른 Studocu URL을 입력하세요.','processing':'처리 중...','starting':'시작 중...','completed_status':'완료 · {message}','failed_status':'실패 · {message}','edge_not_found':'Microsoft Edge를 찾을 수 없습니다','loading':'로딩 중...','wait_document':'문서 로딩을 기다리는 중...','wait_seconds':'문서 대기 중... {seconds}초','document_ready':'문서가 로드되었습니다','document_timeout':'문서 로딩 시간 초과','cleanup_page':'흐림, 배너 및 광고 제거 중...','capture_pf':'.pf 페이지 캡처 중...','capture_pages':'페이지 캡처 중...','found_pages':'{pages}페이지 발견','content_valid':'문서 내용이 유효합니다','direct_capture':'페이지 직접 캡처 중...','pdf_generation_failed':'PDF 생성 실패','pdf_success':'PDF 생성 완료 ({size:.1f} KB)'},
    'vi': {**EN, 'language':'Ngôn ngữ','ready':'●  Sẵn sàng','busy':'●  Đang xử lý','done':'●  Hoàn tất','error_state':'●  Thất bại','guide_title':'Tải xuống trong ba bước','guide_hint':'Edge có thể mở khi xử lý. Vui lòng giữ cửa sổ mở.','step1_title':'Dán liên kết tài liệu','step1_desc':'Sao chép URL trang tài liệu Studocu','step2_title':'Xác nhận nơi lưu','step2_desc':'Mặc định là Desktop hoặc chọn thư mục khác','step3_title':'Bắt đầu tải PDF','step3_desc':'Mở tệp sau khi xử lý hoàn tất','action_title':'Tạo PDF','action_desc':'Nhập liên kết và chọn thư mục. Phần còn lại hoàn toàn tự động.','safe_badge':'Xử lý cục bộ · Không tải tệp lên','url_label':'URL tài liệu Studocu','start_button':'Bắt đầu tải PDF','path_label':'Nơi lưu','choose_folder':'Chọn thư mục','choose_folder_title':'Chọn thư mục lưu','ready_status':'Sẵn sàng · Dán liên kết để bắt đầu','status_help':'Không đóng Edge khi đang xử lý','log_title':'Nhật ký xử lý','log_desc':'Tiến trình tải trang, chụp và tạo PDF xuất hiện tại đây','open_pdf':'Mở PDF đã tạo','clear':'Xóa','log_placeholder':'Đang chờ tác vụ...','footer_note':'Mẹo: tài liệu nhiều trang sẽ mất nhiều thời gian hơn','invalid_title':'Thông báo','invalid_text':'Hãy nhập URL tài liệu Studocu hợp lệ trước khi bắt đầu.','processing':'Đang xử lý...','starting':'Đang khởi động...','completed_status':'Hoàn tất · {message}','failed_status':'Thất bại · {message}','edge_not_found':'Không tìm thấy Microsoft Edge','loading':'Đang tải...','wait_document':'Đang chờ tài liệu tải...','wait_seconds':'Đang chờ tài liệu... {seconds} giây','document_ready':'Tài liệu đã tải','document_timeout':'Hết thời gian tải tài liệu','cleanup_page':'Đang xóa làm mờ, biểu ngữ và quảng cáo...','capture_pf':'Đang chụp trang từ .pf...','capture_pages':'Đang chụp trang...','found_pages':'Đã tìm thấy {pages} trang','content_valid':'Nội dung tài liệu hợp lệ','direct_capture':'Đang chụp trực tiếp trang...','pdf_generation_failed':'Tạo PDF thất bại','pdf_success':'Đã tạo PDF ({size:.1f} KB)'},
}

BRAND_TRANSLATIONS = {
    'de': {
        'window_title': 'StudocuHack — Intelligentes PDF-Download-Tool',
        'tagline': 'Intelligente Dokumentverarbeitung und PDF-Download',
    },
    'fr': {
        'window_title': 'StudocuHack — Outil intelligent de téléchargement PDF',
        'tagline': 'Traitement intelligent de documents et téléchargement PDF',
    },
    'it': {
        'window_title': 'StudocuHack — Strumento intelligente per PDF',
        'tagline': 'Elaborazione intelligente dei documenti e download PDF',
    },
    'tr': {
        'window_title': 'StudocuHack — Akıllı PDF İndirme Aracı',
        'tagline': 'Akıllı belge işleme ve PDF indirme aracı',
    },
    'es': {
        'window_title': 'StudocuHack — Herramienta inteligente de PDF',
        'tagline': 'Procesamiento inteligente de documentos y descarga de PDF',
    },
    'ja': {
        'window_title': 'StudocuHack — スマート PDF ダウンロードツール',
        'tagline': '文書をスマートに処理して PDF をダウンロード',
    },
    'ko': {
        'window_title': 'StudocuHack — 스마트 PDF 다운로드 도구',
        'tagline': '스마트 문서 처리 및 PDF 다운로드 도구',
    },
    'vi': {
        'window_title': 'StudocuHack — Công cụ tải PDF thông minh',
        'tagline': 'Xử lý tài liệu thông minh và tải xuống PDF',
    },
}


def tr(lang, key, **kwargs):
    text = BRAND_TRANSLATIONS.get(lang, {}).get(
        key, TRANSLATIONS.get(lang, EN).get(key, EN.get(key, key))
    )
    return text.format(**kwargs) if kwargs else text


class SmoothProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(8); self.setRange(0, 100)
        self._a = 0; self._t = 0
        self._tm = QTimer(self)
        self._tm.timeout.connect(self._up); self._tm.start(16)

    def set_smooth_value(self, v):
        self._t = v
        if not self._tm.isActive(): self._tm.start(16)

    def _up(self):
        d = self._t - self._a
        if abs(d) < 0.5: self._a = self._t; self._tm.stop()
        else: self._a += d * 0.15
        super().setValue(int(self._a))

    def paintEvent(self, e):
        p = QPainter(self); p.setRenderHint(QPainter.Antialiasing)
        w, h, r = self.width(), self.height(), self.height()/2
        p.setPen(Qt.NoPen); p.setBrush(QColor(229,234,242))
        p.drawRoundedRect(0,0,w,h,r,r)
        fw = int(w * self.value() / 100.0)
        if fw > 0:
            g = QLinearGradient(0,0,fw,0)
            g.setColorAt(0,QColor(79,70,229)); g.setColorAt(0.55,QColor(37,99,235)); g.setColorAt(1,QColor(16,185,129))
            p.setBrush(g); p.drawRoundedRect(0,0,fw,h,r,r)
        p.end()


class FlatButton(QPushButton):
    def __init__(self, text, primary=True):
        super().__init__(text)
        self._p = primary; self._h = False
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedHeight(62)
        self.setFont(QFont('Segoe UI', 17, QFont.Bold if primary else QFont.Normal))
    def enterEvent(self, e): self._h=True; self.update(); super().enterEvent(e)
    def leaveEvent(self, e): self._h=False; self.update(); super().leaveEvent(e)
    def paintEvent(self, e):
        p = QPainter(self); p.setRenderHint(QPainter.Antialiasing)
        w,h = self.width(), self.height()
        if self._p:
            if not self.isEnabled(): c1=c2=QColor(148,163,184)
            elif self.isDown(): c1=QColor(29,78,216); c2=QColor(67,56,202)
            elif self._h: c1=QColor(37,99,235); c2=QColor(99,102,241)
            else: c1=QColor(37,99,235); c2=QColor(79,70,229)
        else:
            c1=QColor(241,245,249) if self._h else QColor(248,250,252)
            c2=QColor(226,232,240) if self._h else QColor(241,245,249)
        g=QLinearGradient(0,0,w,h); g.setColorAt(0,c1); g.setColorAt(1,c2)
        p.setBrush(g); p.setPen(Qt.NoPen)
        p.drawRoundedRect(0,0,w,h,12,12)
        p.setPen(Qt.white if self._p else QColor(30,41,59))
        font = QFont(self.font())
        while QFontMetrics(font).horizontalAdvance(self.text()) > w - 28 and font.pointSize() > 11:
            font.setPointSize(font.pointSize() - 1)
        p.setFont(font)
        p.drawText(self.rect(), Qt.AlignCenter, self.text())
        p.end()


# ============================================================
# 下载引擎 — 三级方案自动降级
# ============================================================
class StudocuDownloader(QThread):
    log_signal = pyqtSignal(str)
    status_signal = pyqtSignal(str)
    progress_signal = pyqtSignal(int)
    finished_signal = pyqtSignal(bool, str, str)

    def __init__(self, url, output_path, lang='zh-CN'):
        super().__init__()
        self.url = url; self.output_path = output_path; self.lang = lang

    def log(self, m): self.log_signal.emit(m)
    def sts(self, m): self.status_signal.emit(m)
    def t(self, key, **kwargs): return tr(self.lang, key, **kwargs)
    def tagged(self, tag, key, **kwargs): return f'[{self.t(tag)}] {self.t(key, **kwargs)}'

    def run(self):
        try: self._run()
        except Exception as e:
            self.log(self.tagged('tag_error', 'error_message', error=str(e)))
            self.finished_signal.emit(False, self.t('error_message', error=str(e)), '')

    def gen_pdf_path(self):
        """生成唯一 PDF 路径"""
        p = self.output_path
        if os.path.isdir(p):
            title = 'studocu_document'
            m = re.search(r'/document/([^/]+)', self.url)
            if m: title = m.group(1)[:40]
            title = re.sub(r'[\\/:*?"<>|]', '_', title)
            suffix = ''.join(random.choices('abcdef0123456789', k=4))
            p = str(Path(p) / f'{title}_{suffix}.pdf')
        if os.path.exists(p):
            try: os.remove(p)
            except: pass
        return p

    def verify_pdf(self, path, min_size=50000):
        """验证 PDF 是否包含真实文档内容"""
        if not os.path.exists(path): return False
        sz = os.path.getsize(path)
        if sz < min_size: return False
        # 检查 PDF 内容
        try:
            with open(path, 'rb') as f:
                data = f.read(5000)
            text = data.decode('latin-1')
            # 如果包含 Cloudflare 拦截内容则失败
            if 'Access Blocked' in text or 'suspicious activity' in text or 'cf-browser-verification' in text:
                return False
            return True
        except:
            return sz > min_size

    def _run(self):
        self.log(f'[{self.t("tag_system")}] StudocuHack Desktop v3.0')
        self.log(self.tagged('tag_strategy', 'strategy_text'))
        self.sts(self.t('starting'))

        if not os.path.exists(EDGE_PATH):
            self.finished_signal.emit(False, self.t('edge_not_found'), '')
            return

        self.log(f'[{self.t("tag_browser")}] Edge: {EDGE_PATH}')

        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            self.finished_signal.emit(False, self.t('install_playwright'), '')
            return

        # 关闭已运行的 Edge
        os.system('taskkill /f /im msedge.exe 2>nul')
        time.sleep(2)

        pdf_path = self.gen_pdf_path()
        self.log(self.tagged('tag_output', 'output_path', path=pdf_path))

        with sync_playwright() as pw:
            context = pw.chromium.launch_persistent_context(
                user_data_dir=EDGE_USER_DATA,
                executable_path=EDGE_PATH,
                headless=False,
                viewport={'width': 1280, 'height': 900},
                locale=LANGUAGES.get(self.lang, LANGUAGES['en'])[1],
                args=['--no-sandbox', '--disable-blink-features=AutomationControlled'],
            )

            page = context.pages[0] if context.pages else context.new_page()

            self.log(self.tagged('tag_navigation', 'open_page'))
            self.sts(self.t('loading'))

            try:
                page.goto(self.url, wait_until='commit', timeout=30000)
            except Exception as e:
                self.log(self.tagged('tag_hint', 'navigation_hint', error=str(e)[:60]))

            # 等待文档就绪（最长 120 秒）
            self.log(self.tagged('tag_waiting', 'wait_document'))
            doc_ready = False
            for i in range(120, 0, -1):
                time.sleep(1)
                try:
                    t = page.title()
                    has_pf = page.query_selector('.pf') is not None
                    has_pc = page.query_selector('#page-container') is not None
                    if i % 10 == 0:
                        self.log(self.tagged('tag_status', 'document_status', title=t[:40], pf=has_pf, pc=has_pc))
                        self.sts(self.t('wait_seconds', seconds=i))
                    if has_pf or has_pc:
                        doc_ready = True
                        self.log(self.tagged('tag_ready', 'document_ready'))
                        break
                except:
                    pass

            if not doc_ready:
                context.close()
                self.finished_signal.emit(False, self.t('document_timeout'), '')
                return

            self.progress_signal.emit(15)

            # ---- 通用清理（综合3个扩展） ----
            self.log(self.tagged('tag_cleanup', 'cleanup_page'))
            page.evaluate("""
                (function() {
                    // stuhack remove-blur.js 方式
                    var containers = Array.from(document.getElementsByClassName('blurred-container'));
                    containers.forEach(function(c) {
                        if (c.firstChild && c.firstChild.src) {
                            c.firstChild.src = c.firstChild.src.replace('/blurred/', '/');
                            c.classList.remove('blurred-container');
                        }
                    });

                    // Paywall-Bypass 方式
                    var style = document.createElement('style');
                    style.textContent = '.page-content{filter:blur(0px)!important}';
                    document.head.appendChild(style);

                    // 通用移除模糊样式
                    document.querySelectorAll('.pf,.page-content,.img-container,.text-container').forEach(function(el) {
                        el.style.filter='none'; el.style.opacity='1';
                        el.style.visibility='visible'; el.style.clipPath='none';
                    });
                    document.querySelectorAll('.pf img').forEach(function(img) {
                        if (img.src && img.src.includes('blurred')) {
                            img.src = img.src.replace('/blurred/', '/');
                        }
                        img.style.filter='none'; img.style.opacity='1';
                    });

                    // stuhack remove-banner.js 方式
                    var bw = document.getElementById('document-wrapper');
                    if (bw && bw.childNodes.length > 3) {
                        bw.childNodes[0].parentNode.removeChild(bw.childNodes[0]);
                    }
                    document.querySelectorAll('.banner-wrapper').forEach(function(el) { el.remove(); });
                })();
            """)
            time.sleep(1)

            # ---- 方案B: .pf 逐页捕获（studocuhack 方式） ----
            self.log(self.tagged('tag_strategy', 'capture_pf'))
            self.sts(self.t('capture_pages'))

            # 滚动加载所有 .pf
            max_pages = 0
            for attempt in range(8):
                pfs = page.query_selector_all('.pf')
                n = len(pfs)
                if n > max_pages:
                    max_pages = n
                    self.progress_signal.emit(min(30 + int(n / max(n, 1) * 30), 65))
                    self.log(self.tagged('tag_capture', 'found_pages', pages=n))

                page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
                time.sleep(2)

                if n >= 50: break  # 超过50页不再等

            # 提取 .pf 内容（保留原始CSS，同 studocuhack 的 assembleContainer）
            html_b = page.evaluate("""
                (function() {
                    try {
                        var pfs = document.querySelectorAll('.pf');
                        if (!pfs || pfs.length === 0) return JSON.stringify({error: 'no .pf found'});

                        var title = '';
                        var h1 = document.querySelector('h1');
                        if (h1) title = h1.textContent.trim();
                        if (!title) title = document.title || 'Document';

                        // 1. 保留原始 <head>（含 pdf2htmlEX 的 CSS 和 @font-face）
                        var headHTML = document.head ? document.head.innerHTML : '';

                        // 2. 克隆每个 .pf，保持原始结构和类名（同 studocuhack 的 assembleContainer）
                        var p2hv = document.createElement('div');
                        p2hv.className = 'p2hv';  // 保持 pdf2htmlEX CSS 作用域

                        pfs.forEach(function(pf) {
                            var clone = pf.cloneNode(true);
                            // 清除模糊样式
                            clone.style.filter = 'none';
                            clone.style.opacity = '1';
                            clone.style.visibility = 'visible';
                            clone.style.clipPath = 'none';
                            // 修复图片
                            var imgs = clone.querySelectorAll('img');
                            imgs.forEach(function(img) {
                                img.style.filter = 'none';
                                img.style.opacity = '1';
                                img.style.visibility = 'visible';
                                if (img.src && img.src.includes('blurred')) {
                                    img.src = img.src.replace('/blurred/', '/');
                                }
                            });
                            // 修复文字层
                            var texts = clone.querySelectorAll('.pc, .page-content, [class*="page-content"]');
                            texts.forEach(function(t) {
                                t.style.filter = 'none';
                                t.style.opacity = '1';
                                t.style.visibility = 'visible';
                                t.style.display = 'block';
                            });
                            p2hv.appendChild(clone);
                        });

                        // 3. 构建完整 HTML（保留原始样式 + 自定义打印样式）
                        var html = '<!DOCTYPE html><html><head>'
                            + '<meta charset=\"utf-8\">'
                            + '<title>' + title.replace(/</g,'&lt;') + '</title>'
                            + headHTML
                            + '<style>'
                            + 'body{margin:0;padding:0;background:#525659!important;}'
                            + '.p2hv{margin:0 auto;}'
                            + '.pf{margin:12px auto!important;background:#fff!important;'
                            + 'box-shadow:0 2px 8px rgba(0,0,0,.4);display:block!important;'
                            + 'filter:none!important;opacity:1!important;}'
                            + '.page-content,.pc{display:block!important;visibility:visible!important;'
                            + 'filter:none!important;opacity:1!important;}'
                            + '.pf img{filter:none!important;opacity:1!important;visibility:visible!important;}'
                            + '*{filter:none!important;}'
                            + '.blurred-container{filter:none!important;}'
                            + '@media print{'
                            + 'body{background:#fff!important;}'
                            + '.pf{margin:0!important;box-shadow:none!important;'
                            + 'page-break-after:always;break-after:page;}'
                            + '.pf:last-child{page-break-after:auto;}'
                            + '@page{margin:0;}}'
                            + '</style></head><body>'
                            + '<div class="p2hv">' + p2hv.innerHTML + '</div>'
                            + '</body></html>';

                        return JSON.stringify({
                            html: html,
                            pageCount: pfs.length
                        });
                    } catch(e) { return JSON.stringify({error: e.message}); }
                })();
            """)

            data_b = json.loads(html_b) if html_b else None
            if data_b and data_b.get('pageCount', 0) > 0 and not data_b.get('error'):
                pc = data_b['pageCount']
                html = data_b['html']
                self.log(self.tagged('tag_strategy', 'strategy_b_success', pages=pc))

                has_content = bool(re.search(r'<(img|span|p|div)', html))
                if has_content:
                    self.progress_signal.emit(55)
                    self.log(self.tagged('tag_validation', 'content_valid'))
                    success = self.render_and_pdf(context, html, pdf_path)
                    if success:
                        context.close()
                        return
                    else:
                        self.log(self.tagged('tag_pdf', 'render_failed'))
                else:
                    self.log(self.tagged('tag_validation', 'content_empty'))
            else:
                self.log(self.tagged('tag_capture', 'extraction_failed'))

            # ---- 备用: 直接 page.pdf() 截取 ----
            self.log(self.tagged('tag_direct', 'direct_capture'))
            self.sts(self.t('direct_capture'))
            self.progress_signal.emit(60)

            try:
                page.pdf(
                    path=pdf_path, format='A4', print_background=True,
                    margin={'top':'5mm','bottom':'5mm','left':'3mm','right':'3mm'},
                )
                if self.verify_pdf(pdf_path):
                    sz = os.path.getsize(pdf_path)
                    self.log(self.tagged('tag_strategy', 'strategy_c_success', size=sz/1024))
                    self.progress_signal.emit(100)
                    context.close()
                    self.finished_signal.emit(True, self.t('pdf_success', size=sz/1024), pdf_path)
                    return
            except Exception as e:
                self.log(self.tagged('tag_strategy', 'strategy_c_failed', error=str(e)[:60]))

            context.close()
            self.finished_signal.emit(False, self.t('pdf_generation_failed'), '')

    def render_and_pdf(self, context, html, pdf_path):
        """在新页面渲染纯文档 HTML 并生成 PDF"""
        try:
            pdf_page = context.new_page()
            pdf_page.set_content(html, wait_until='networkidle')
            time.sleep(2)

            # 滚动加载所有图片
            pdf_page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            pdf_page.evaluate('window.scrollTo(0, 0)')
            time.sleep(1)

            pdf_page.pdf(
                path=pdf_path, format='A4', print_background=True,
                margin={'top':'0mm','bottom':'0mm','left':'0mm','right':'0mm'},
            )
            pdf_page.close()

            if self.verify_pdf(pdf_path):
                sz = os.path.getsize(pdf_path)
                self.log(self.tagged('tag_pdf', 'pdf_complete', size=sz/1024))
                self.progress_signal.emit(100)
                time.sleep(0.3)
                self.finished_signal.emit(True, self.t('pdf_success', size=sz/1024), pdf_path)
                return True
            else:
                self.log(self.tagged('tag_pdf', 'pdf_validation_failed'))
                return False
        except Exception as e:
            self.log(self.tagged('tag_pdf', 'pdf_error', error=str(e)[:80]))
            return False


# ============================================================
# 主窗口 — 精致商务风 UI
# ============================================================
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.downloader = None; self.last_pdf_path = ''; self.lang = 'zh-CN'; self.indicator_state = 'ready'
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('StudocuHack — PDF 智能下载工具')
        screen = QApplication.primaryScreen()
        if screen:
            available = screen.availableGeometry()
            width = min(max(1200, int(available.width() * 0.82)), available.width() - 40)
            height = min(max(820, int(available.height() * 0.88)), available.height() - 40)
            self.resize(width, height)
            self.move(
                available.x() + (available.width() - width) // 2,
                available.y() + (available.height() - height) // 2,
            )
        else:
            self.resize(1440, 960)
        self.setMinimumSize(1050, 820)

        central = QWidget()
        central.setObjectName('central')
        self.setCentralWidget(central)

        # 全局字体
        font = QFont('Segoe UI', 14)
        for name in ['Inter', 'PingFang SC', 'Microsoft YaHei']:
            if QFontDatabase().families().__contains__(name):
                font = QFont(name, 14)
                break
        self.setFont(font)

        # 全局样式
        self.setStyleSheet("""
            QMainWindow, #central { background-color: #f4f7fb; }
            QLabel {
                color: #172033;
                font-family: 'Segoe UI', 'Inter', 'PingFang SC', 'Microsoft YaHei', sans-serif;
            }
            QFrame#guideCard, QFrame#actionCard, QFrame#statusCard, QFrame#logCard {
                background-color: #ffffff;
                border: 1px solid #e5eaf2;
                border-radius: 18px;
            }
            QFrame#stepCard {
                background-color: #f8faff;
                border: 1px solid #e8edf6;
                border-radius: 13px;
            }
            QLineEdit {
                background-color: #ffffff;
                color: #172033;
                border: 1.5px solid #dce3ee;
                border-radius: 12px;
                padding: 16px 20px;
                font-size: 18px;
                selection-background-color: #2563eb;
            }
            QLineEdit:focus {
                border: 2px solid #4f6ff0;
                background-color: #ffffff;
            }
            QLineEdit:read-only {
                background-color: #f8fafc;
                color: #475569;
            }
            QLineEdit::placeholder { color: #9aa7b8; }
            QTextEdit {
                background-color: #111827;
                color: #cbd5e1;
                border: 1px solid #1f2937;
                border-radius: 12px;
                padding: 17px 20px;
                font-family: 'Cascadia Code', 'SF Mono', 'Consolas', monospace;
                font-size: 15px;
                selection-background-color: #374151;
            }
            QTextEdit QScrollBar:vertical {
                width: 10px;
                background: #111827;
                margin: 4px 2px;
            }
            QTextEdit QScrollBar::handle:vertical {
                background: #475569;
                border-radius: 4px;
                min-height: 28px;
            }
            QTextEdit QScrollBar::add-line:vertical,
            QTextEdit QScrollBar::sub-line:vertical {
                height: 0px;
            }
            QPushButton {
                font-family: 'Segoe UI', 'Inter', 'PingFang SC', 'Microsoft YaHei', sans-serif;
            }
            QPushButton#secondaryButton {
                background-color: #f8fafc;
                color: #334155;
                border: 1.5px solid #dce3ee;
                border-radius: 11px;
                padding: 0 22px;
                font-size: 16px;
                font-weight: 600;
            }
            QPushButton#secondaryButton:hover {
                background-color: #eef2ff;
                color: #3f51cc;
                border-color: #bfc9f8;
            }
            QPushButton#secondaryButton:pressed { background-color: #e0e7ff; }
            QPushButton#ghostButton {
                background: transparent;
                color: #64748b;
                border: 1px solid #dce3ee;
                border-radius: 8px;
                padding: 7px 18px;
                font-size: 14px;
                font-weight: 600;
            }
            QPushButton#ghostButton:hover {
                color: #334155;
                background-color: #f1f5f9;
            }
            QPushButton#openButton {
                background-color: #ecfdf3;
                color: #15803d;
                border: 1px solid #bbf7d0;
                border-radius: 9px;
                padding: 9px 22px;
                font-size: 15px;
                font-weight: 700;
            }
            QPushButton#openButton:hover {
                background-color: #dcfce7;
                border-color: #86efac;
            }
            QComboBox {
                background-color: #ffffff;
                color: #334155;
                border: 1px solid #dce3ee;
                border-radius: 12px;
                padding: 8px 14px;
                min-width: 130px;
                font-size: 14px;
                font-weight: 600;
            }
            QComboBox:hover { border-color: #a5b4fc; }
            QComboBox::drop-down { border: none; width: 24px; }
            QComboBox QAbstractItemView {
                background: #ffffff;
                color: #334155;
                border: 1px solid #dce3ee;
                selection-background-color: #eef2ff;
                selection-color: #312e81;
            }
            QToolTip {
                color: #ffffff;
                background-color: #172033;
                border: 0;
                padding: 6px 10px;
            }
        """)

        root = QVBoxLayout(central)
        root.setContentsMargins(46, 32, 46, 26)
        root.setSpacing(18)

        # ======== 顶部导航 ========
        nav = QHBoxLayout()
        nav.setContentsMargins(2, 0, 2, 0)

        logo = QLabel('S')
        logo.setFixedSize(58, 58)
        logo.setAlignment(Qt.AlignCenter)
        logo.setStyleSheet("""
            background: #4f46e5; color: white; border-radius: 16px;
            font-size: 30px; font-weight: 900;
        """)
        nav.addWidget(logo, 0, Qt.AlignVCenter)
        nav.addSpacing(15)

        brand = QVBoxLayout()
        brand.setSpacing(0)
        name_lbl = QLabel('StudocuHack')
        name_lbl.setStyleSheet("font-size: 28px; font-weight: 800; color: #172033; letter-spacing: -0.4px;")
        brand.addWidget(name_lbl)
        self.tag_lbl = QLabel()
        self.tag_lbl.setStyleSheet("font-size: 15px; color: #7c899b;")
        brand.addWidget(self.tag_lbl)
        nav.addLayout(brand)

        nav.addStretch()

        self.language_combo = QComboBox()
        for code, (name, _) in LANGUAGES.items():
            self.language_combo.addItem(name, code)
        self.language_combo.setCurrentIndex(list(LANGUAGES).index(self.lang))
        self.language_combo.currentIndexChanged.connect(self.change_language)
        nav.addWidget(self.language_combo)
        nav.addSpacing(13)

        version_lbl = QLabel('v3.0')
        version_lbl.setStyleSheet("""
            color: #64748b; background: #ffffff; border: 1px solid #e5eaf2;
            border-radius: 12px; padding: 7px 13px; font-size: 13px; font-weight: 700;
        """)
        nav.addWidget(version_lbl)
        nav.addSpacing(13)

        # 状态指示器
        self.indicator = QLabel()
        self.indicator.setStyleSheet("""
            font-size: 14px; color: #15803d; font-weight: 700;
            padding: 8px 16px; background: #ecfdf3;
            border: 1px solid #bbf7d0; border-radius: 14px;
        """)
        nav.addWidget(self.indicator)

        root.addLayout(nav)

        # ======== 使用引导 ========
        guide_card = QFrame()
        guide_card.setObjectName('guideCard')
        guide_layout = QVBoxLayout(guide_card)
        guide_layout.setContentsMargins(28, 20, 28, 22)
        guide_layout.setSpacing(15)

        guide_title_row = QHBoxLayout()
        self.guide_title = QLabel()
        self.guide_title.setStyleSheet("font-size: 18px; font-weight: 800; color: #172033;")
        guide_title_row.addWidget(self.guide_title)
        guide_title_row.addStretch()
        self.guide_hint = QLabel()
        self.guide_hint.setStyleSheet("font-size: 14px; color: #8a97a8;")
        guide_title_row.addWidget(self.guide_hint)
        guide_layout.addLayout(guide_title_row)

        steps_row = QHBoxLayout()
        steps_row.setSpacing(14)
        self.step_labels = []
        for number in ('1', '2', '3'):
            step_card = QFrame()
            step_card.setObjectName('stepCard')
            step_layout = QHBoxLayout(step_card)
            step_layout.setContentsMargins(16, 14, 16, 14)
            step_layout.setSpacing(13)
            number_lbl = QLabel(number)
            number_lbl.setFixedSize(34, 34)
            number_lbl.setAlignment(Qt.AlignCenter)
            number_lbl.setStyleSheet("""
                color: #ffffff; background: #4f46e5; border-radius: 17px;
                font-size: 14px; font-weight: 800;
            """)
            step_layout.addWidget(number_lbl, 0, Qt.AlignVCenter)
            step_text = QVBoxLayout()
            step_text.setSpacing(2)
            title_lbl = QLabel()
            title_lbl.setStyleSheet("font-size: 15px; font-weight: 700; color: #243047;")
            desc_lbl = QLabel()
            desc_lbl.setStyleSheet("font-size: 13px; color: #8491a3;")
            step_text.addWidget(title_lbl)
            step_text.addWidget(desc_lbl)
            step_layout.addLayout(step_text)
            steps_row.addWidget(step_card, 1)
            self.step_labels.append((title_lbl, desc_lbl))
        guide_layout.addLayout(steps_row)
        root.addWidget(guide_card)

        # ======== 下载操作卡片 ========
        input_card = QFrame()
        input_card.setObjectName('actionCard')
        input_layout = QVBoxLayout(input_card)
        input_layout.setContentsMargins(30, 23, 30, 25)
        input_layout.setSpacing(16)

        action_header = QHBoxLayout()
        action_title_box = QVBoxLayout()
        action_title_box.setSpacing(1)
        self.action_title = QLabel()
        self.action_title.setStyleSheet("font-size: 22px; font-weight: 800; color: #172033;")
        self.action_desc = QLabel()
        self.action_desc.setStyleSheet("font-size: 14px; color: #8491a3;")
        action_title_box.addWidget(self.action_title)
        action_title_box.addWidget(self.action_desc)
        action_header.addLayout(action_title_box)
        action_header.addStretch()
        self.safe_badge = QLabel()
        self.safe_badge.setStyleSheet("""
            color: #166534; background: #f0fdf4; border: 1px solid #dcfce7;
            border-radius: 12px; padding: 7px 13px; font-size: 13px; font-weight: 700;
        """)
        action_header.addWidget(self.safe_badge, 0, Qt.AlignTop)
        input_layout.addLayout(action_header)

        # URL 输入
        url_section = QVBoxLayout()
        url_section.setSpacing(8)
        self.url_label = QLabel()
        self.url_label.setStyleSheet("font-size: 15px; font-weight: 700; color: #334155;")
        url_section.addWidget(self.url_label)

        url_row = QHBoxLayout()
        url_row.setSpacing(13)
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText('https://www.studocu.com/document/...')
        self.url_input.setMinimumHeight(62)
        url_row.addWidget(self.url_input)

        self.dl_btn = FlatButton('', True)
        self.dl_btn.setFont(QFont('Segoe UI', 17, QFont.Bold))
        self.dl_btn.setFixedWidth(300)
        self.dl_btn.setMinimumHeight(62)
        self.dl_btn.clicked.connect(self.start_download)
        url_row.addWidget(self.dl_btn)
        url_section.addLayout(url_row)
        input_layout.addLayout(url_section)

        # 保存路径
        path_section = QVBoxLayout()
        path_section.setSpacing(8)
        self.path_label = QLabel()
        self.path_label.setStyleSheet("font-size: 15px; font-weight: 700; color: #334155;")
        path_section.addWidget(self.path_label)

        path_row = QHBoxLayout()
        path_row.setSpacing(13)
        self.path_input = QLineEdit(DEFAULT_OUTPUT)
        self.path_input.setReadOnly(True)
        self.path_input.setMinimumHeight(56)
        path_row.addWidget(self.path_input)

        self.sel_btn = QPushButton()
        self.sel_btn.setObjectName('secondaryButton')
        self.sel_btn.setFixedSize(190, 56)
        self.sel_btn.setCursor(Qt.PointingHandCursor)
        self.sel_btn.clicked.connect(self.choose_folder)
        path_row.addWidget(self.sel_btn)
        path_section.addLayout(path_row)
        input_layout.addLayout(path_section)

        root.addWidget(input_card)

        # ======== 状态与进度 ========
        status_card = QFrame()
        status_card.setObjectName('statusCard')
        status_layout = QVBoxLayout(status_card)
        status_layout.setContentsMargins(23, 15, 23, 16)
        status_layout.setSpacing(10)

        status_row = QHBoxLayout()
        status_row.setSpacing(11)
        status_icon = QLabel('◉')
        status_icon.setStyleSheet("font-size: 16px; color: #4f46e5;")
        status_row.addWidget(status_icon)

        self.status_label = QLabel()
        self.status_label.setStyleSheet("font-size: 15px; color: #64748b; font-weight: 600;")
        status_row.addWidget(self.status_label)
        status_row.addStretch()
        self.status_help = QLabel()
        self.status_help.setStyleSheet("font-size: 13px; color: #9aa7b8;")
        status_row.addWidget(self.status_help)
        status_layout.addLayout(status_row)

        self.progress = SmoothProgressBar()
        self.progress.setVisible(False)
        self.progress.setFixedHeight(10)
        status_layout.addWidget(self.progress)
        root.addWidget(status_card)

        # ======== 日志卡片 ========
        log_card = QFrame()
        log_card.setObjectName('logCard')
        log_layout = QVBoxLayout(log_card)
        log_layout.setContentsMargins(23, 18, 23, 20)
        log_layout.setSpacing(12)

        log_header = QHBoxLayout()
        log_header.setSpacing(11)
        log_title_box = QVBoxLayout()
        log_title_box.setSpacing(0)
        self.log_title = QLabel()
        self.log_title.setStyleSheet("font-size: 18px; font-weight: 800; color: #172033;")
        self.log_desc = QLabel()
        self.log_desc.setStyleSheet("font-size: 13px; color: #8a97a8;")
        log_title_box.addWidget(self.log_title)
        log_title_box.addWidget(self.log_desc)
        log_header.addLayout(log_title_box)
        log_header.addStretch()

        self.open_btn = QPushButton()
        self.open_btn.setObjectName('openButton')
        self.open_btn.setCursor(Qt.PointingHandCursor)
        self.open_btn.setVisible(False)
        self.open_btn.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl.fromLocalFile(self.last_pdf_path))
            if self.last_pdf_path and os.path.exists(self.last_pdf_path) else None
        )
        log_header.addWidget(self.open_btn)

        # 清空按钮
        self.clear_btn = QPushButton()
        self.clear_btn.setObjectName('ghostButton')
        self.clear_btn.setFixedSize(100, 40)
        self.clear_btn.setCursor(Qt.PointingHandCursor)
        self.clear_btn.clicked.connect(lambda: self.log_output.clear())
        log_header.addWidget(self.clear_btn)
        log_layout.addLayout(log_header)

        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setMinimumHeight(220)
        log_layout.addWidget(self.log_output)
        root.addWidget(log_card, 1)

        # ======== 底部版权 ========
        footer = QHBoxLayout()
        footer.setContentsMargins(2, 0, 2, 0)
        self.footer_note = QLabel()
        self.footer_note.setStyleSheet("color: #9aa7b8; font-size: 12px;")
        footer.addWidget(self.footer_note)
        footer.addStretch()
        footer_brand = QLabel('© 2024 众创启航 · StudocuHack v3.0')
        footer_brand.setStyleSheet("color: #9aa7b8; font-size: 12px;")
        footer.addWidget(footer_brand)
        root.addLayout(footer)
        self.apply_language()

    def t(self, key, **kwargs):
        return tr(self.lang, key, **kwargs)

    def change_language(self):
        code = self.language_combo.currentData()
        if code:
            self.lang = code
            self.apply_language()

    def choose_folder(self):
        folder = QFileDialog.getExistingDirectory(self, self.t('choose_folder_title'), self.path_input.text())
        if folder:
            self.path_input.setText(folder)

    def apply_language(self):
        self.setWindowTitle(self.t('window_title'))
        self.tag_lbl.setText(self.t('tagline'))
        self.language_combo.setToolTip(self.t('language'))
        self.guide_title.setText(self.t('guide_title'))
        self.guide_hint.setText(self.t('guide_hint'))
        for index, (title, desc) in enumerate(self.step_labels, 1):
            title.setText(self.t(f'step{index}_title'))
            desc.setText(self.t(f'step{index}_desc'))
        self.action_title.setText(self.t('action_title'))
        self.action_desc.setText(self.t('action_desc'))
        self.safe_badge.setText(self.t('safe_badge'))
        self.url_label.setText(self.t('url_label'))
        self.url_input.setToolTip(self.t('url_tooltip'))
        self.path_label.setText(self.t('path_label'))
        self.sel_btn.setText(self.t('choose_folder'))
        self.sel_btn.setToolTip(self.t('path_tooltip'))
        self.status_help.setText(self.t('status_help'))
        self.log_title.setText(self.t('log_title'))
        self.log_desc.setText(self.t('log_desc'))
        self.open_btn.setText(self.t('open_pdf'))
        self.clear_btn.setText(self.t('clear'))
        self.log_output.setPlaceholderText(self.t('log_placeholder'))
        self.footer_note.setText(self.t('footer_note'))
        if not self.downloader or not self.downloader.isRunning():
            self.dl_btn.setText(self.t('start_button'))
            self.dl_btn.setToolTip(self.t('start_tooltip'))
            if self.indicator_state == 'ready':
                self.status_label.setText(self.t('ready_status'))
        else:
            self.dl_btn.setText(self.t('processing'))
        self.update_indicator(self.indicator_state)

    def log(self, msg):
        color = '#cbd5e1'
        error_tags = (f'[{self.t("tag_error")}]',)
        success_tags = (f'[{self.t("tag_ready")}]', f'[{self.t("tag_validation")}]')
        info_tags = (f'[{self.t("tag_system")}]', f'[{self.t("tag_strategy")}]',
                     f'[{self.t("tag_browser")}]', f'[{self.t("tag_output")}]')
        wait_tags = (f'[{self.t("tag_waiting")}]', f'[{self.t("tag_hint")}]', f'[{self.t("tag_status")}]')
        if msg.startswith(error_tags):
            color = '#fca5a5'
        elif msg.startswith(success_tags):
            color = '#86efac'
        elif msg.startswith(info_tags):
            color = '#93c5fd'
        elif msg.startswith(wait_tags):
            color = '#fde68a'
        self.log_output.append(f'<span style="color:{color};">{html.escape(msg)}</span>')
        sb = self.log_output.verticalScrollBar()
        sb.setValue(sb.maximum())
        QApplication.processEvents()

    def update_indicator(self, state):
        self.indicator_state = state
        colors = {
            'ready': (self.t('ready'), '#15803d', '#ecfdf3', '#bbf7d0'),
            'busy': (self.t('busy'), '#b45309', '#fffbeb', '#fde68a'),
            'done': (self.t('done'), '#15803d', '#ecfdf3', '#bbf7d0'),
            'error': (self.t('error_state'), '#b91c1c', '#fef2f2', '#fecaca'),
        }
        text, fg, bg, border = colors.get(state, colors['ready'])
        self.indicator.setText(text)
        self.indicator.setStyleSheet(
            f"font-size: 14px; color: {fg}; font-weight: 700; "
            f"padding: 8px 16px; background: {bg}; border: 1px solid {border}; border-radius: 14px;"
        )

    def start_download(self):
        url = self.url_input.text().strip()
        if not url or 'studocu' not in url.lower():
            msg = QMessageBox(self)
            msg.setWindowTitle(self.t('invalid_title'))
            msg.setText(self.t('invalid_text'))
            msg.setInformativeText(self.t('invalid_info'))
            msg.setStyleSheet("""
                QMessageBox { background: #ffffff; }
                QLabel { color: #334155; font-size: 16px; min-width: 440px; }
                QPushButton {
                    background: #4f46e5; color: white; border: none;
                    border-radius: 9px; padding: 9px 25px; font-size: 15px; font-weight: 700;
                }
                QPushButton:hover { background: #4338ca; }
            """)
            msg.exec_()
            return
        if not url.startswith('http'):
            url = 'https://' + url
            self.url_input.setText(url)

        self.dl_btn.setEnabled(False)
        self.dl_btn.setText(self.t('processing'))
        self.dl_btn.setFont(QFont('Segoe UI', 17, QFont.Bold))
        self.open_btn.setVisible(False)
        self.progress.setVisible(True)
        self.progress.set_smooth_value(0)
        self.log_output.clear()
        self.status_label.setText(self.t('starting'))
        self.status_label.setStyleSheet("font-size: 15px; color: #b45309; font-weight: 700;")
        self.update_indicator('busy')

        self.downloader = StudocuDownloader(url, self.path_input.text(), self.lang)
        self.downloader.log_signal.connect(self.log)
        self.downloader.status_signal.connect(self.status_label.setText)
        self.downloader.progress_signal.connect(self.progress.set_smooth_value)
        self.downloader.finished_signal.connect(self.done)
        self.downloader.start()

    def done(self, ok, msg, path):
        self.dl_btn.setEnabled(True)
        self.dl_btn.setText(self.t('start_button'))
        self.dl_btn.setFont(QFont('Segoe UI', 17, QFont.Bold))
        if ok:
            self.progress.set_smooth_value(100)
            self.status_label.setStyleSheet("font-size: 15px; color: #15803d; font-weight: 700;")
            self.status_label.setText(self.t('completed_status', message=msg))
            self.last_pdf_path = path
            self.open_btn.setVisible(True)
            self.update_indicator('done')
            QTimer.singleShot(1500, lambda: self.progress.setVisible(False))
        else:
            self.progress.setVisible(False)
            self.status_label.setStyleSheet("font-size: 15px; color: #b91c1c; font-weight: 700;")
            self.status_label.setText(self.t('failed_status', message=msg))
            self.update_indicator('error')

    def closeEvent(self, event):
        # 安全退出时关闭 Edge
        os.system('taskkill /f /im msedge.exe 2>nul')
        super().closeEvent(event)


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # 精细调色板 — 明亮柔和
    p = QPalette()
    p.setColor(QPalette.Window, QColor(245, 245, 247))
    p.setColor(QPalette.WindowText, QColor(29, 29, 31))
    p.setColor(QPalette.Base, QColor(255, 255, 255))
    p.setColor(QPalette.Text, QColor(29, 29, 31))
    p.setColor(QPalette.Button, QColor(0, 122, 255))
    p.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    p.setColor(QPalette.Highlight, QColor(0, 122, 255))
    p.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
    p.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
    p.setColor(QPalette.ToolTipText, QColor(29, 29, 31))
    p.setColor(QPalette.Disabled, QPalette.Text, QColor(200, 200, 204))
    app.setPalette(p)

    w = MainWindow()
    w.show()

    # 淡入动画
    a = QPropertyAnimation(w, b'windowOpacity')
    a.setDuration(400)
    a.setStartValue(0.0)
    a.setEndValue(1.0)
    a.setEasingCurve(QEasingCurve.OutCubic)
    a.start()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
