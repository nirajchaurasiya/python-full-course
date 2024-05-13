import json

file_name = "youtube.txt"


def load_data():
    try:
        with open(file_name, "r") as file:
            test = json.load(file)
            # print(type(test))
            return test

    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open(file_name, "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    # print("------------------------------------")
    # print("Index | Video name | Video duration")
    print("-" * 100)
    print("All Videos")
    print("-" * 100)
    for index, video in enumerate(videos, start=1):
        print(f"| {index} | {video['name']} | {video['time']}")
        print("-" * 100)


def add_video(videos):
    video_name = input("Enter video name:\n")
    video_time = input("Enter video time:\n")
    videos.append({"name": video_name, "time": video_time})
    save_data_helper(videos)
    print("-" * 100)
    print("Video Added Successfully")
    print("-" * 100)


def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update:\n"))

    if 1 <= index <= len(videos):
        name = input("Enter the new video name:\n")
        time = input("Enter the new video time:\n")

        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
        print("-" * 100)
        print("Video Updated Successfully")
        print("-" * 100)
    else:
        print("Invalid index selected")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete:\n"))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
        print("-" * 100)
        print("Video Deleted Successfully")
        print("-" * 100)
    else:
        print("Invalid index selected")


def main():

    videos = load_data()

    while True:
        print("\nYoutube Manager | Choose an Option")
        print("1. List all youtube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Enter your choice:\n")
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
