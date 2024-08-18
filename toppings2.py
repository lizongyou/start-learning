#建立专辑函数
def make_album(singer, album, songs=None):
    if songs:
        album = {'singer': singer,
                 'album': album,
                 'songs':songs}
    else:
        album = {'singer': singer,
                 'album': album}
    return album

album_collection = []

#录入专辑
while True:
    while True:
        singer_input = input("输入你最喜欢的歌手：（若想取消收录请输入“确定”）：")
        if singer_input == "确定":
            break
        album_input = input("输入他的一个专辑（若想取消收录请输入“确定”）：")
        if album_input == "确定":
            break
        songs_input = input("输入该专辑中收入的歌曲的数量（若想取消收录请输入“确定”）：")
        if songs_input == "确定":
            break

        album_dict = make_album(singer_input, album_input, songs_input)
        album_collection.append(album_dict)

    print("您收入的专辑有：")
    print(f"{album_dict}")
    confirmation = input("是否需要添加（是/否）：")
    if confirmation == "否":
        break
