def convert(face2):
    face2=face2.replace(":(","🙁").replace(":)","🙂")
    print(face2)

def main():
    face=input("say something and make a face! ")
    convert(face)

main()
