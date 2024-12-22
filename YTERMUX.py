import yt_dlp



print ("\n\n")
print ("\33[1;49;33m##############################################################")
print ("\33[1;49;33m#  ######  ##             ##   ########  #########         ###")
print ("\33[1;49;33m##  ####  ########  ########  #  ######  #########  ######   #")
print ("\33[1;49;34m###  ##  #########  ########  ###  ####  #########  ######   #")
print ("\33[1;49;34m####    ##########  ########  #####  ##  #########         ###")
print ("\33[1;49;34m#####  ###########  ########  #####  ##  #########  ##########")
print ("\33[1;49;31m#####  ###########  ########  ###  ####  #########  ##########")
print ("\33[1;49;31m#####  ###########  ########  #  ######  #########  ##########")                                                 print ("\33[1;49;31m#####  ###########  ########   ########         ##  ##########")                                                 print ("\33[1;49;31m##############################################################\33m")

print("\n\n\n\033[1;49;33mFrase de gracia, devoción y fe:\033[0m")
print("\n\n\033[1;49;34m'El Señor Jesucristo viene pronto'\033[0m")
print("\033[1;49;31mMateo 24:25; Author: Belial;\033[0m\n\n")



print("\33[0;49;32m\n\nINF/YTDLP-TERMUX:\33[0m\n\nYTDLP-TERMUX ejecuta de forma legible YT-DLP.\n\n")
print("\33[0;49;32mFRASE DE GRACIA, DEVOCIÓN Y FE:\33[0m 'EL SEÑOR JESUCRISTO VIENE PRONTO'")
print("\33[0;49;32m\n\nEjemplo:\n\nURL: \33[0mhttps://m.youtube.com/watch?v=B4XlyzvjRIU&pp=ygUNTEVYWSBQQU5URVJSQQ%3D%3D\n")
u = input("\33[0;49;32m\nURL: \33[0m")
print("\n\n\33[0;49;32mEjemplo:\33[0m\n\n\33[0;49;32mRESOLUCIÓN:\33[0m\n\n1080 \33[0;49;32m==>\33[0m HD")
r = input("\n\n\33[0;49;32mRESOLUCIÓN: \33[0m")
print("\33[0;49;32m\n\nEjemplo:\n\nRUTA DE ALMACENAMIENTO:\33[0m /data/data/com.termux/files/home/storage/downloads/YTERMUX\n\n\33[0>
rd = input("\33[0;49;32m\n\nRUTA DE ALMACENAMIENTO: \33[0m")
print("\n\n")
ydl_opts = {



        'format':'bv[height='+r+']+ba',
'outtmpl':rd+'/%(title)s.%(ext)s',
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



with yt_dlp.YoutubeDL(ydl_opts) as ydl:

    ydl.add_post_processor(YTERMUX(), when='pre_process')
    error_code = ydl.download(u)








