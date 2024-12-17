import yt_dlp



print ("\n\n")
print ("\33[1;49;33m##############################################################")
print ("\33[1;49;33m#  ######  ##             ##   ########  #########         ###")
print ("\33[1;49;33m##  ####  ########  ########  #  ######  #########  ######   #")
print ("\33[1;49;34m###  ##  #########  ########  ###  ####  #########  ######   #")
print ("\33[1;49;34m####    ##########  ########  #####  ##  #########         ###")
print ("\33[1;49;34m#####  ###########  ########  #####  ##  #########  ##########")
print ("\33[1;49;31m#####  ###########  ########  ###  ####  #########  ##########")
print ("\33[1;49;31m#####  ###########  ########  #  ######  #########  ##########")
print ("\33[1;49;31m#####  ###########  ########   ########         ##  ##########")
print ("\33[1;49;31m##############################################################\33m")





print("\33[0;49;32m\n\nINF/YTDLP-TERMUX:\33[0m\n\nYTDLP-TERMUX ejecuta de forma legible YT-DLP.\n\n")
print("\33[0;49;32mEjemplo:\n\nURL: \33[0mhttps://m.youtube.com/watch?v=B4XlyzvjRIU&pp=ygUNTEVYWSBQQU5URVJSQQ%3D%3D\n")
u = input("\33[0;49;32m\nURL: \33[0m")
print("\n\n\33[0;49;32mEjemplo:\33[0m\n\n\33[0;49;32mRESOLUCIÓN:\33[0m\n\n1080 \33[0;49;32m==>\33[0m HD")
r = input("\n\n\33[0;49;32mRESOLUCIÓN: \33[0m")
print("\n")

ydl_opts = {
        'format':'bv[height='+r+']+ba',


  'final_ext': 'mp4',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',

        }],




}










class YTERMUX(yt_dlp.postprocessor.PostProcessor):
    def run(self, info):
        self.to_screen('\33[0;49;32mYTDLP-TERMUX/DOWNLOAD:\33[0m\33[0;49;34mInitializing\33[0m...')
        return [], info





with yt_dlp.YoutubeDL(ydl_opts) as ydl
