# YTERMUX
YTERMUX ejecuta de forma legible la codificación de video urlstreaming de YT-DLP al formato almacenable de video MP4.

<h2>INSTALACIÓN:</h2>
<p>~ $ yes | pkg update && yes | pkg upgrade</p>
<p>~ $ yes | pkg install python</p>
<p>~ $ pip install yt-dlp</p>
<p>~ $ yes | pkg install ffmpeg</p>
<p>~ $ yes | pkg install git</p>
<p>~ $ git clone https://github.com/wolfkrypter/YTERMUX.git</p>
<p>~ $ cd YTERMUX</p>

<h2>EJECUCIÓN:</h2>
<p>~/YTERMUX $ python YTERMUX.py</p>
<img src="https://i.imgur.com/BWNHZKx.jpeg" alt="YTERMUX">
<h3>Almacenamiento:</h3>
<p>~ $ yes | termux-setup-storage</p>
<p>~ $ cd storage/downloads</p>
<p>~/storage/downloads $ mkdir YTERMUX</p>
<p>~/storage/downloads $ cd YTERMUX</p>
<p>~/.../downloads/YTERMUX $ python /data/data/com.termux/files/home/YTERMUX/YTERMUX.py</p>
<img src="https://i.imgur.com/h728pFX.jpeg" alt="YTERMUX">

<h5>INF/TERMUX:</h5>
<p>Con la ejecución de YTERMUX en un directorio de tal manera, obtiene las extracciones directamente a tal directorio.</p>
<h2>DESINSTALACIÓN:</h2>

<p>~ $ yes | rm -r YTERMUX</p>
<p>~ $ yes | pkg uninstall python</p>
<p>~ $ yes | pkg uninstall ffmpeg</p>
<p>~ $ yes | pip uninstall yt-dlp</p>
<p>~ $ yes | pkg uninstall git </p>
<p>~ $ yes | apt autoremove</p>

