from pymongo import MongoClient

from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")

# Not a good idea to include id and password in code files

db = client["ytmanager"]

video_collection = db["videos"]

print(video_collection)

def list_videos():
    print("-"*60)
    for video in video_collection.find():
        print(f"ID: {video["_id"]}, Name: {video["name"]}, Time: {video["time"]}")
    print("-"*60)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})


def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id':ObjectId(video_id)},
        {"$set":{"name":new_name,"time":new_time}}
        )

def delete_video(video_id):
    video_collection.delete_one({"_id":ObjectId(video_id)})

def main():
    while True:
        print("\nYoutube manager app with DB")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete a video")
        choice = input("Enter your choices: ")

        if choice == "1":
            list_videos()

        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")

            add_video(name, time)

        elif choice == "3":
            list_videos()
            video_id = input("Enter the video ID: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")

            update_video(video_id, name, time)

        elif choice == "4":
            list_videos()
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)

        elif choice == "5":
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()
