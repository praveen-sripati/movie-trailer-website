import media
import fresh_tomatoes

# Instance of class Movie as toy_story_4
toy_story_4 = media.Movie(
    "Toy Story 4",
    "When a new toy called \"Forky\" joins Woody and the gang,"
    " a road trip alongside old and new friends reveals how big"
    " the world can be for a toy.",
    "http://t0.gstatic.com/"
    "images?q=tbn:ANd9GcShcfz6m_J2ifhGZJJ3WMwZ_yykXe6Cgq6oi7SyAvtptrUkD_Kk",
    "https://youtu.be/LDXYRzerjzU")

# Instance of class Movie as dark_phoenix
dark_phoenix = media.Movie(
    "Dark Phoenix",
    "Jean Grey begins to develop incredible powers that corrupt and"
    " turn her into a Dark Phoenix."
    " Now the X-Men will have to decide if the life of a team member is worth"
    " more than all the people living in the world.",
    "https://upload.wikimedia.org/wikipedia/en/9/9e/"
    "Dark_Phoenix_%28film%29.png",
    "https://youtu.be/1-q8C_c-nlM")

# Instance of class Movie as detective_pikachu
detective_pikachu = media.Movie(
    "Detective Pikachu",
    "A young man joins forces with Detective Pikachu to unravel"
    " the mystery behind his father's disappearance."
    " Chasing clues through the streets of Ryme City,"
    " the dynamic duo soon discover a devious plot"
    " that poses a threat to the Pokemon universe.",
    "http://t0.gstatic.com/"
    "images?q=tbn:ANd9GcQGFrQd3ez_nmjQhnH7F3vyJUbDogMKNqoU6nCd-7rJ3ZzgprZo",
    "https://youtu.be/1roy4o4tqQM")

# Instance of class Movie as aladdin
aladdin = media.Movie(
    "Aladdin",
    "Aladdin, the clever hero of Agrabah, continues his adventures with the"
    " help of his fiancee Princess Jasmine, his pet monkey Abu, Magic Carpet,"
    " Iago the greedy parrot, and of course his best friend"
    " the semi-cosmic Genie.",
    "http://t2.gstatic.com/"
    "images?q=tbn:ANd9GcS0iX7-Xf5HNESuF97hUIUaATgShTXTz-LUI5qkflHEs7KZY-du",
    "https://youtu.be/TzWlGGokGeE")

# Instance of class Movie as how_to_train_your_dragon_3
how_to_train_your_dragon_3 = media.Movie(
    "How to Train Your Dragon: The Hidden World",
    "Hiccup, Toothless and their fellow dragon-riders continue"
    " to rescue captured dragons in order to bring them"
    " to Berk and its bustling dragon and human utopia.",
    "https://contentserver.com.au/assets/653022_p13022653_p_v8_ab.jpg",
    "https://youtu.be/SkcucKDrbOI")

# Instance of class Movie as hellboy
hellboy = media.Movie(
    "Hellboy",
    "Based on the graphic novels by Mike Mignola, Hellboy,"
    " caught between the worlds of the supernatural"
    " and human, battles an ancient sorceress bent on revenge.",
    "http://t2.gstatic.com/"
    "images?q=tbn:ANd9GcQ5DBLNqpMvWEzlVkZsQN-mF_D-i6v0fI19aYk3Y0JZ6Vdrl04T",
    "https://youtu.be/cU55vwvEJmk")

# Instance of class Movie as avengers_endgame
avengers_endgame = media.Movie(
    "Avengers: Endgame",
    "After the devastating events of Avengers: Infinity War (2018),"
    " the universe is in ruins. With the help of remaining allies,"
    " the Avengers assemble once more in order to undo"
    " Thanos' actions and restore order to the universe.",
    "http://t3.gstatic.com/"
    "images?q=tbn:ANd9GcT7lbt-11YvVHCYw55oDCcOxXeKF6VaPOrf9rRFINXaq3WWsbo6",
    "https://youtu.be/hA6hldpSTF8")

# Instance of class Movie as spiderman_ffh
spiderman_ffh = media.Movie(
    "Spider-Man: Far From Home",
    "Peter Parker and his friends go on summer vacation to Europe,"
    " where Peter finds himself trying to fight off a new foe, Mysterio,"
    " who as his name indicates may not be all that he appears.",
    "http://t3.gstatic.com/"
    "images?q=tbn:ANd9GcQNaTUqq1CGnigfm7fLvUOfdqyV6OrHtXHTXrlx190CjoRbDxy6",
    "https://youtu.be/DYYtuKyMtY8")

# Instance of class Movie as godzilla_kotm
godzilla_kotm = media.Movie(
    "Godzilla: King of the Monsters",
    "The crypto-zoological agency Monarch faces off against"
    " a battery of god-sized monsters, including the mighty Godzilla,"
    " who collides with Mothra, Rodan, and his ultimate nemesis,"
    " the three-headed King Ghidorah.",
    "http://t3.gstatic.com/"
    "images?q=tbn:ANd9GcQV775HY-S42WZDI_GaKh_LEseI0Q8NCwpy_EwgEclwjOJsdgml",
    "https://youtu.be/wVDtmouV9kM")

movies = [
    toy_story_4,
    dark_phoenix,
    detective_pikachu,
    aladdin,
    avengers_endgame,
    how_to_train_your_dragon_3,
    hellboy,
    godzilla_kotm,
    spiderman_ffh
    ]
fresh_tomatoes.open_movies_page(movies)
