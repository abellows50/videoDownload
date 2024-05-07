import PyInstaller.__main__

PyInstaller.__main__.run([
    'app.py',
    '--name=YouTubeDownloader',
    '--onefile',
    '--windowed',
    '-F',
])