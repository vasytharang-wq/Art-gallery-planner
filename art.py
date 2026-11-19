class ArtGallery:
    def __init__(self, gallery_name):
        self.gallery_name = gallery_name
        self.artworks = []
        print(f"Welcome! '{self.gallery_name}' is now open for the day.")

    def add_artwork(self, title, artist):
        artwork = {"title": title, "artist": artist}
        self.artworks.append(artwork)
        print(f"Added '{title}' by {artist} to the collection.")

    def remove_artwork(self, title):
        for art in self.artworks:
            if art["title"].lower() == title.lower():
                self.artworks.remove(art)
                print(f"Removed '{art['title']}' from the collection.")
                return
        print(f"Sorry, '{title}' was not found in the gallery.")

    def show_artworks(self):
        print(f"\n--- {self.gallery_name} Collection ---")
        if len(self.artworks) == 0:
            print("The gallery is currently empty.")
        else:
            for index, art in enumerate(self.artworks, start=1):
                print(f"{index}. '{art['title']}' by {art['artist']}")
        print("------------------------------------")

    def __del__(self):
        print(f"\nClosing '{self.gallery_name}'. Thanks for visiting!")

my_gallery = ArtGallery("Lincoln High Art Gallery")

while True:
    print("\nChoose an option:")
    print("1. Add Artwork")
    print("2. Remove Artwork")
    print("3. Show Artworks")
    print("4. Quit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        title = input("Enter artwork title: ")
        artist = input("Enter student artist's name: ")
        my_gallery.add_artwork(title, artist)

    elif choice == "2":
        title = input("Enter the title of the artwork to remove: ")
        my_gallery.remove_artwork(title)

    elif choice == "3":
        my_gallery.show_artworks()

    elif choice == "4":
        del my_gallery
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")