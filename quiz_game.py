#! /usr/bin/env python3

questions = [
    {
        "prompt": "When was the Air Jordan line of shoes released?",
        "options": ["A. 1985", "B. 2000", "C. 1981", "D. 1992"],
        "answer": "A",
        "explaination":
            "The Air Jordan line of shoes was first released in 1985. "
            "This iconic line of athletic footwear was created by Nike in collaboration with basketball legend "
            "Michael Jordan. \nThe release of the Air Jordan sneakers revolutionized the sneaker industry, "
            "setting new standards for design, performance, and style.\n"
            "The debut Air Jordan model, the Air Jordan 1, "
            "quickly became a cultural phenomenon and laid the foundation for a highly successful and enduring line of sneakers."
    },
    { 
        "prompt": "\nWho are Hiroshi Fujiwara, Tinker Hatfield and Nathan VanHook?",
        "options": ["A. Sneakerheads with the largest collections", "B. Collectible Nike sneaker designers","C. Adidas marketing experts", "D. Creators of the brands The Bathing Ape, Stussy, and Supreme."],
        "answer": "B",
        "explaination":
            "Sneakerheads know their shoe designers and often buy only from the designers they admire. \n"
            "Hatfield was hired in 1981 as a corporate architect for Nike, but switched to sneakers in 1985. \n"
            "Fukiwara is known as the father of Harajuku style in Japan, and VanHook is on his way to being the next big Nike designer."
    },
    { 
        "prompt": "\nWho was the first pro basketball player to have a signature shoe designed for them?",
        "options": ["A. Michael Jordan", "B. Kareem Abdul-Jabbar", "C. Magic Johnson", "D. Clyde Drexler"],
        "answer": "B",
        "explaination":
            "By 1971, just two years after joining the NBA, Kareem Abdul-Jabbar was already a superstar. \n"
            "Drafted first overall by the Milwaukee Bucks in 1969, Jabbar scored 29 points in his first game and won Rookie of the Year. \n"
            "His second year he was named MVP. Adidas gave Jabbar his own signature shoe, setting a precedence for all sneaker makers to follow."
    },
    { 
        "prompt": "\nTrue or False: Nike’s original name was Dimension Six",
        "options": ["A. True","B. False"],
        "answer": "B",
        "explaination":
            "The Nike name and the Nike Swoosh had been appearing on sneakers since 1972, but it’s original name – \n"
            "Blue Ribbon Sports – wasn’t officially changed until 1978. The name \"Dimension Six\" was Phil Knight’s idea, \nbut it never stuck."
    },
    { 
        "prompt": "\nTrue or False: The sneaker brands Puma and Adidas were created out of a brothers’ argument.",
        "options": ["A. True", "B. False"],
        "answer": "A",
        "explaination":
            "In 1948, shoemakers and brothers, Rudolf and Adolf Dassler, had an argument. \n"
            "Rudolf left the family shoe company and started his own. Adolf renamed his company adidas (a shortening of his nickname, \"Adi Dassler\"), \n"
            "and Rudolf named his Puma. The first, and longest-standing, sneaker rivalry was born."
    },
    { 
        "prompt": "\nWhat is the largest sneakerhead summit in the world?",
        "options": ["A. H-Town Sneaker Summit", "B. Fresh Out Of The Box","C. Sneakercon","D. Complexcon"],
        "answer": "A",
        "explaination":
            "It may not have been the very first (Fresh Out The Box in NYC was), but \n"
            "the H-Town Sneaker Summit has grown over the years to become the biggest sneaker gathering known to man. \n"
            "Held bi-annually, H-Town anchors NBA All-Star weekend and continues to attract both new sneakerheads and \n"
            "the heaviest of heavy hitters in the sneaker community."
    },
    {
        "prompt": "\nIf a sneakerhead is someone who's obsessed with sneakers, what is a \"hypebeast\" sneakerhead?",
        "options": ["A. A sneakerhead who buys only one brand of shoe", "B. A sneakerhead who only talks about the shoes he or she owns","C. A sneakerhead who only buys shoes based on buzz around its release",  "D. A sneakerhead who on>
        "answer": "C",
        "explaination":
            "A \"hypebeast\" is someone that only follows the hype around some sneakers than others. \n"
            "Technically, they only pay attention to more buzzed-about shoe releases because they’re \"cooler.\""
    },
    { 
        "prompt": "\nWhat is Niketalk?",
        "options": ["A. A gossip column for Nike sneakers","B. Nike’s sneakerhead magazine", "C. A podcast about Nike information and news", "D. An official Nike blog and forum for sneakersheads"],
        "answer": "D",
        "explaination":
            "Niketalk started back in 1999, just when blogs were beginning to take shape. \n"
            "Until then, sneakerhead talk was limited to chat rooms and message boards. \n"
            "Niketalk brought sneakheads for sneak peeks of new releases, release dates and more. It’s still going strong."
    },
    { 
        "prompt": "\nAccording to sneakerheads, what is a \"retro\" sneaker?",
        "options": ["A. A shoe that's re-released for sale due to its popularity", "B. A shoe that was created before 1985", "C. A shoe that looks old and worn out", "D. A shoe release that takes design traits from the past fused with >
        "answer": "A",
        "explaination":
            "Sneakerhead terminology not only tracks how shoes sell, but when they're sold, as well. \n"
            "\"Retro\" sneakers are models that sold out on prior releases"
    },
    { 
        "prompt": "\nTrue or False: Michael Jordan was fined $5,000 per game because the black and red Air Jordan Air 1 were not regulation court shoes.",
        "options": ["A. True", "B. False"],
        "answer": "A",
        "explaination":
            "Nike paid Jordan’s $5,000 fine for each game he played wearing the black and red Jordans. \n"
            "It was the best investment Nike ever made, as Air Jordan's quickly became Nike's best-selling shoes of all time."
    }
]


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("\nEnter your answer:").upper()
        if answer == question["answer"]:
            print("Correct, nicee!!\n")
            score += 1
        else:
            print("Wrong, That ain't it. The answer was", question["answer"],"\n")
            print(question["explaination"], "\n")

    print(f"You got {score} out of {len(questions)} questions correct.")

run_quiz(questions)
