books_list=[]
authors_set=set()
books_dict={}

books_list.append("Python Programming") 
authors_set.add("John Smith") 
books_dict["Python Programming"] = "John Smith"
books_list.append("Data Structures and Algorithms") 
authors_set.add("Jane Doe") 
books_dict["Data Structures and Algorithms"] = "Jane Doe"
books_list.append("Machine Learning Basics")
authors_set.add("Alice Johnson") 
new_items = ['''“Ethereal Echoes: A Fantasy Adventure”,
“Love in the Time of Stardust”,
“Murder on the Midnight Express: A Mystery Noir”,
“Quantum Dreams: Sci-Fi Chronicles”,
“The Enchanted Garden: A Whimsical Romance”“Ethereal Echoes”,
“Love in the Time of Stardust”,
“Murder on the Midnight Express”,
“Quantum Dreams”,
“The Enchanted Garden”,
“Whispers of the Forgotten Forest”,
“The Clockwork Conspiracy”,
“Sapphire Skies and Stolen Dreams”,
“The Alchemist’s Daughter”,
“Echoes of Eternity”,
“Midnight at the Enigma Café”,
“The Quantum Paradox”,
“Crimson Tides and Silver Serpents”,
“The Starlight Cipher”,
“The Velvet Labyrinth”,
“The Oracle’s Veil”,
“The Forgotten Atlas”,
“Harmony in Discord”,
“The Celestial Mechanism”,
“The Whimsical Wanderer”,
“The Arcane Almanac”,
“The Midnight Mirage”,
“The Labyrinth of Lost Legends”,
“The Quantum Quill”,
“The Alabaster Aegis”,
“The Echoing Eon”,
“The Obsidian Oath”,
“The Astral Atlas”,
“The Enchanted Emporium”,
“The Sapphire Serpent”,
“The Midnight Mandala”,
“The Celestial Codex”,
“The Whimsical Warden”,
“The Crimson Compass”,
“The Forgotten Fable”,
“The Alchemical Archive”,
“The Echoing Echo”,
“The Obsidian Oracle”,
“The Astral Alchemy”,
“The Enchanted Echo”,
“The Sapphire Scroll”,
“The Midnight Mirage”,
“The Celestial Cipher”,
“The Whimsical Watchmaker”,
“The Quantum Quill”,
“The Crimson Crown”,
“The Forgotten Forest”,
“The Alchemical Amulet”,
“The Echoing Enigma”,
“The Obsidian Odyssey”,
“The Astral Archive”,
“The Enchanted Eon”,
“The Sapphire Star”''']

# Append multiple items using a loop
for item in new_items:
    books_list.append(item)

print(books_list)
books_dict["Machine Learning Basics"] = "Alice Johnson"

search_title=input("enter the title of the book to search:")
if search_title in books_list:
    print(f"Book found!Author:{books_dict[search_title]}")
else:
    print("book not found!")

print("list of Books:")
for book in books_list:
    print(book)

remove_title = input("Enter the title of the book to remove or else enter to skip: ")
if remove_title in books_list:
    remove_author = books_dict[remove_title]
    books_list.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dict[remove_title]
    print("Book removed successfully!")
    print("Books available:",books_list)

else:
    print("book not found!")