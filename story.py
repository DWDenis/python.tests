def first_meeting():
    print("Hey 👋, you new here, ain't ya?")
    print("Sooo 👉👈, where are you from? 😊")
    global place
    place = input()
    print("Yooo that's crazy, never heard of it. 😐")

def know_each_oder():
    print("Since you kinda new here, let me guide you.")
    print("By the way, I'm Fairy \"THE MIGHTY RAVEN\" 🌩️🐦‍⬛🌩️")
    print("It is quite my pleasure to be acquaintance with you")
    print("So what is your name?")
    global name
    name = input()
    know_name = print(f"Good name \"{name}\", it does rolls well in the tongue, does it have any meaning? ")
    answer = input("Yes/No?")
    if answer.lower == "Yes":
        print("Cool, cool")
    else:
        print("There's no way, come on go look if you find something comeback!")




def i_tried(did:bool) -> str:
    if did == True:
        print("I did")
    else:
        return("really?")
    
i_tried(True)
      