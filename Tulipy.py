from pytube import YouTube
from pytube import Playlist
import pyperclip
import validators

def linha():
    print("=" * 128)

def menu_principal():
    linha()
    print("Menu de Opções\n1. Baixar vídeo um a um.\n2. Baixar uma Playlist.\n3. Sair.")
    opcao = input("Menu desejado: ")
    linha()
    return opcao

def sub_menu():
    linha()
    print("Submenu de opções\n1. Baixar em formato MP4.\n2. Baixar em formato MP3.\n3. Sair.")
    opcao = input("Submenu desejado: ")
    linha()
    return opcao

def mensagem_de_erro(nome_do_usuario, e):
    print(f"ERRO {e}. Me desculpe, {nome_do_usuario}, peço que tente novamente.")
    
def baixar_video_mp4(nome_do_usuario, url):
    try:
        yt = YouTube(url)
        # Faz o download do vídeo em formato MP4
        print(f"Seu download em formato MP4 está sendo realizado, {nome_do_usuario}. Aguarde alguns segundos.")
        print("Baixando...")
        yt.streams.get_highest_resolution().download(output_path="musicas/musicas mp4")
        print("Download concluído!")
    except Exception as e:
        # Mostra uma mensagem de erro para o usuário
        mensagem_de_erro(nome_do_usuario, e)

def baixar_video_mp3(nome_do_usuario, url):
    try:
        yt = YouTube(url)
        # Faz o download do áudio em formato MP3
        print(f"Seu download em formato MP3 está sendo realizado, {nome_do_usuario}. Aguarde alguns segundos.")
        print("Baixando...")
        yt.streams.get_audio_only().download(output_path="musicas/musicas mp3")
        print("Download concluído!")
    except Exception as e:
        # Mostra uma mensagem de erro para o usuário
        mensagem_de_erro(nome_do_usuario, e)

def baixar_playlist_mp4(nome_do_usuario, url):
    try:
        playlist = Playlist(url)
        # Implemente o código para baixar os vídeos da playlist aqui
        print(f"Total de vídeos: {len(playlist)}.\nBaixando a playlist.")
        for video in playlist.videos:
            video.streams.first().download(output_path="Playlist/Playlist mp4")

    except Exception as e:
        # Mostra uma mensagem de erro para o usuário
        mensagem_de_erro(nome_do_usuario, e)

def baixar_playlist_mp3(nome_do_usuario, url):
    try:
        playlist = Playlist(url)
        # Implemente o código para baixar os vídeos da playlist aqui
        print(f"Total de vídeos: {len(playlist)}.\nBaixando a playlist.")
        for video in playlist.videos:
            video.streams.get_audio_only().download(output_path="Playlist/Playlist mp3")
    except Exception as e:
        # Mostra uma mensagem de erro para o usuário
        mensagem_de_erro(nome_do_usuario, e)

def main():
    linha()
    print("\nOlá, eu sou a Tulipy, sua assistente de conversão de vídeos do Youtube. Informe seu nome para nos conhecermos melhor. ")
    nome = str(input("Meu nome é: ").lower()).capitalize()
    print(f"Estou animada de te conhecer {nome}, apresentarei o menu de opções de serviços que podemos oferecer a você.\n")
    linha()
    op = menu_principal()
    while op != "3":
        if op == "1":
            while True:
                print(f"{nome}, irei pegar o último item copiado para iniciar o download. Enquanto eu compilo o arquivo, relaxe e aproveite o momento.")
                confirmacao = input("Caso ainda não tenha pegado um link do Youtube, utilize essa confirmação para copiar um e quando estiver pronto digite OK: ").lower()
                url = pyperclip.paste()
                # Aloca na variável url a função pyperclip com a cópia do usuário

                # Verifica se a URL é válida
                if not validators.url(url):
                    print(f"{nome}, essa URL é inválida! Por favor, informe uma URL válida do YouTube.")
                    continue  # volta para o início do loop

                op_submenu = sub_menu()
                if op_submenu == "1":
                    baixar_video_mp4(nome, url)
                elif op_submenu == "2":
                    baixar_video_mp3(nome, url)
                elif op_submenu == "3":
                    break
                linha()
                pgt = input("Quer baixar mais um vídeo? (s/n): ").lower()
                if pgt != "s":
                    break    

            op = menu_principal()
        elif op == "2":
            while True:
                print(f"{nome}, vamos pegar o link da playlist para iniciar o download. Enquanto eu compilo os arquivos, relaxe e aproveite o momento.")
                confirmacao = input("Caso ainda não tenha pegado um link da playlist do Youtube, utilize essa confirmação para copiar um e quando estiver pronto digite OK: ").lower()
                url = pyperclip.paste()
                # Aloca na variável url a função pyperclip com a cópia do usuário

                # Verifica se a URL é válida
                if not validators.url(url):
                    print(f"{nome}, essa URL é inválida! Por favor, informe uma URL válida da playlist do YouTube.")
                    continue  # volta para o início do loop
                
                op_submenu = sub_menu()
                if op_submenu == "1":
                    baixar_playlist_mp4(nome, url)
                elif op_submenu == "2":
                    baixar_playlist_mp3(nome,url)
                elif op_submenu == "3":
                    break
                linha()
                pgt = input("Quer baixar mais uma playlist? (s/n): ").lower()
                if pgt != "s":
                    break
                
            op = menu_principal()

    print(f"Agradeço pelo uso, {nome}! Volte sempre.")
    linha()

main()