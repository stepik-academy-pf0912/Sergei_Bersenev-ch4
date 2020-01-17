videos = [
    {"id": 1, "title": "Squadron 42. Trailer 2018", "link": "R9GQ3R0lJXQ"},
    {"id": 2, "title": "Squadron 42. Trailer 2015", "link": "8EC4WHPxnrk"},
    {"id": 3, "title": "Star Citizen. Anvil - Carrack", "link": "Vm4t1jUBT1U"},
    {"id": 4, "title": "Star Citizen. Drake Interplanetary - Kraken", "link": "to1kDbR4L4I"},
    {"id": 5, "title": "Star Citizen. Последний Контракт", "link": "b56DX5SF5sM"},
    {"id": 6, "title": "Star Citizen. Лорвиль (Бегущий По Лезвию)", "link": "pA6P2WserfU"}
]

playlists = [
    {"id": 1, "title": "Trailers", "videos": [1, 2]},
    {"id": 2, "title": "Ships", "videos": [3, 4]},
    {"id": 3, "title": "Fan work", "videos": [5, 6]}
]

welcome_text_main_menu = "===== Приложение в разработке =====\n" \
               "Введите '1' чтобы посмотреть все видео.\n" \
               "Введите '2' чтобы посмотреть плейлисты.\n" \
               "Введите 'q' или 'quit' чтобы выйти.\n"


def welcome_text_video_menu():
    print("Выберите номер видео для просмотра:")
    for i in videos:
        print(f"{i['id']}. {i['title']}")
    print()


def welcome_text_playlists_menu():
    print("Выберите номер плейлиста для просмотра:")
    for i in playlists:
        print(f"{i['id']}. {i['title']} ({len(i['videos'])} видео)")
    print()


def print_video(id, number = ''):
    print(f"{number}{videos[id - 1]['title']}\n"
          f"http://youtu.be/{videos[id - 1]['link']}\n")


while True:
    print(welcome_text_main_menu)
    menu_select = input()

    if menu_select == '1':
        welcome_text_video_menu()
        while True:
            video_select = input()
            try:
                video_select = int(video_select)
            except ValueError:
                print("Требуется ввести числовой номер видео, попробуйте еще раз :)\n")
                welcome_text_video_menu()
                continue
            if not 1 <= video_select <= len(videos):
                print("Такого видео у нас нет, попробуйте еще раз :)")
                welcome_text_video_menu()
                continue
            else:
                print("Ваше видео:\n")
                print_video(video_select)
                print("Приятного просмотра!\n")
                break

    elif menu_select == '2':
        welcome_text_playlists_menu()
        while True:
            playlist_select = input()
            try:
                playlist_select = int(playlist_select)
            except ValueError:
                print("Требуется ввести числовой номер плейлиста, попробуйте еще раз :)\n")
                welcome_text_playlists_menu()
                continue
            if not 1 <= playlist_select <= len(playlists):
                print("Такого видео у нас нет, попробуйте еще раз :)")
                welcome_text_playlists_menu()
                continue
            else:
                print(f"{playlists[playlist_select - 1]['title']}:")
                count = 1
                for i in playlists[playlist_select - 1]['videos']:
                    print()
                    print_video(i, str(count) + ' ')
                    count += 1
                print("Приятного просмотра!\n")
                break

    elif menu_select == 'q' or menu_select == 'quit':
        break

    else:
        print("Нет таких вариантов выбора, попробуйте еще раз :)\n")