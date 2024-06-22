import random
import requests
import os


def generate(long):
    kata = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(long):
        acak = random.choice(kata)
        password += acak
    return password

def quotes():
    kata = ["Coding like poetry should be short and concise. ― Santosh Kalwar", 
            "It’s not a bug; it’s an undocumented feature. ― Anonymous",
            "First, solve the problem. Then, write the code. – John Johnson",
            "Code is like humor. When you have to explain it, it’s bad. – Cory House",
            "Make it work, make it right, make it fast. – Kent Beck",
            "Clean code always looks like it was written by someone who cares. — Robert C. Martin",
            "Of course, bad code can be cleaned up. But it’s very expensive.” — Robert C. Martin"
            ]
    keluaran = random.choice(kata)
    return keluaran

def math():
    asal = "x+-"
    a = random.randint(1, 100)
    b = random.choice(asal)
    c = random.randint(1, 100)
    kali = f"{a} {b} {c} =....?"
    return kali

def dictionary(name):
    brainroot_dictionary = {
    "BRAINROOT": "Istilah ini belum spesifik dikenal sebagai slang populer, tapi bisa diartikan sebagai akar dari pemikiran atau ide-ide dasar yang membentuk pola pikir seseorang.",
    "SKIBIDI": "Awalnya dari lagu 'Skibidi' oleh Little Big, istilah ini menjadi populer melalui media sosial seperti TikTok. Biasanya merujuk pada gerakan tari atau suasana yang enerjik dan menyenangkan yang terkait dengan lagu tersebut.",
    "RIZZ": "Singkatan dari 'karisma,' istilah ini sering digunakan untuk menggambarkan pesona seseorang atau kemampuannya untuk menarik orang lain, terutama dalam konteks romantis. Mirip dengan memiliki daya tarik atau keahlian dalam berinteraksi sosial.",
    "CAP": "Slang untuk 'bohong' atau 'tidak benar.' Biasanya digunakan untuk menunjukkan ketidakpercayaan terhadap pernyataan seseorang. Misalnya, 'That's cap' berarti 'Itu bohong.'",
    "BET": "Slang yang digunakan untuk menyetujui sesuatu atau menyatakan kepastian. Misalnya, 'You coming to the party?' 'Bet,' yang artinya 'Pasti.'",
    "YEET": "Istilah yang digunakan untuk menggambarkan tindakan melempar sesuatu dengan kuat atau untuk mengekspresikan kegembiraan atau antusiasme. Misalnya, 'He yeeted the ball across the field' atau hanya berteriak 'Yeet!' saat bersemangat.",
    "NO CAP": "Digunakan untuk menegaskan bahwa apa yang dikatakan adalah benar atau serius, tanpa kebohongan. Misalnya, 'I'm really good at basketball, no cap.'",
    "GHOSTING": "Istilah untuk menghilang dari komunikasi secara tiba-tiba tanpa penjelasan, terutama dalam konteks hubungan atau pertemanan. Misalnya, seseorang yang berhenti membalas pesan tanpa alasan yang jelas.",
    "FOMO": "Singkatan dari 'Fear Of Missing Out,' yaitu rasa cemas atau takut ketinggalan sesuatu yang menyenangkan atau penting yang sedang terjadi.",
    "BUSSIN'": "Istilah yang digunakan untuk menggambarkan sesuatu yang sangat enak atau luar biasa. Sering digunakan untuk makanan. Misalnya, 'This pizza is bussin'."
}
    name = name.upper()

    if name in brainroot_dictionary.keys():
        return brainroot_dictionary[name]
    else:
        return "tidak ada di dict"

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def memes(topic):
    if topic == "Random":
        random_meme=random.randint(1, 10)
        if random_meme in [1, 4, 7]:
            return "images/animals/" + random.choice(os.listdir("images/animals"))
        elif random_meme in [2, 5, 8]:
            return "images/programan/" + random.choice(os.listdir("images/programan"))
        elif random_meme in [3, 6, 9]:
            return "images/relatable/" + random.choice(os.listdir("images/relatable"))
        else:
            return "images/dark/" + random.choice(os.listdir("images/dark"))

    elif topic == "animals":
        return "images/animals/" + random.choice(os.listdir("images/animals"))

    elif topic == "coding":
        return "images/programan/" + random.choice(os.listdir("images/programan"))

    elif topic == "relatable":
        return "images/relatable/" + random.choice(os.listdir("images/relatable"))


    elif topic == "help":
        return "$meme = menampilkan meme dengan topik yang acak(ada kemungkinan mendapatkan meme dengan topik DARK)\n$meme animals = menampilkan meme dengan topic hewan\n$meme coding = menampilkan meme dengan topic coding\n$meme relatable = menampilkan meme yang relate dengan kehidupan\n$meme help = memberitahu hal yang bisa dilakukan oleh $meme"

  
