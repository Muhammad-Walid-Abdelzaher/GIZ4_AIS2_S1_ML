import os


def create_folders(path):

    if not os.path.exists(path):

        os.makedirs(path)

    for i in range(1, 21):

        inner_path = os.path.join(path, "dir_" + str(i))

        if not os.path.exists(inner_path):

            os.makedirs(inner_path)


if __name__ == "__main__":
    path = r"C:\Users\Muhammad Walid\Python\DEPI\GIZ4_AIS2_S1_ML\GIZ4_AIS2_S1_ML\src\Python\session_5\code\tmp_directory"
    create_folders(path)
