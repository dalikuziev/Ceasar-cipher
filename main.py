from emoji import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a',
            'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
play = "yes"
while play == "yes":
  direction = input("Malumotni yashirmoqchi bo'lsangiz 'encode' deb yozing, "
                    "yashirilgan malumotni ochmoqchi bo'lsangiz 'decode' deb yozing: ")
  while direction != "encode" and direction != "decode":
    direction = input("qayta kiriting: ")
  text = input("Habarni kiriting: ").lower()
  shift = int(input("Sirli raqamni kiriting: "))
  if shift > 26:
    shift = shift % 26
  if direction == "decode":
    shift = shift*(-1)
  def caesar(direction, f_text, f_shift):
    new_text = ""
    for letter in text:
      if letter in alphabet:
        position = alphabet.index(letter) + shift
        new_text += alphabet[position]
      else:
        new_text += letter
    print(new_text)
  caesar(direction, text, shift)
  play = input("Yana ma'lumot kiritasizmi? yes/no: ")
