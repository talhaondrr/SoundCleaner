import os
dataset_folder = "/Users/ahmetozturk/Desktop/Human Activity Recognition - Video Dataset"
def list_all_videos_in_dataset():
    if not os.path.exists(dataset_folder):
        print(f"Error: The folder '{dataset_folder}' does not exist.")
        return
    video_files = []
    for root, dirs, files in os.walk(dataset_folder):
        for file in files:
            if file.endswith(('.mp4', '.avi', '.mkv', '.mov')):
                video_files.append(os.path.join(root, file))
    if not video_files:
        print("No video files found in the dataset folder.")
    else:
        print("Found the following video files in the dataset folder and its subfolders:")
        for video_file in video_files:
            print(video_file)
list_all_videos_in_dataset()
