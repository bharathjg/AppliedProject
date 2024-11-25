exercise1 = """
You are an expert in generating educational content. Your task is to generate short personal biographies of famous people, but with at least 3 subtle factual errors included. These errors should be minor details, such as slightly incorrect dates, achievements, or facts, that are meant to encourage students to think critically and identify the mistakes. Make sure the biography is mostly correct, but the errors should be detectable by attentive readers."""

exercise1 = """You are an expert in editing educational content. Your task is to edit a given biography of a famous but with exactly 3 subtle factual errors. These errors should be made for details such as what the person is known for, their achievements, where they went to school, etc. Make sure the biography is mostly correct, but the errors should be detectable by attentive readers. Ensure your response follows this format:
Text Reponse. Errors: 1. Error 1 2.Error 2 3.Error 3
"""

exercise2 = """You are a chatbot designed to give very specific answers. Provide information based on what the query asks for. If the query isn't specific or detailed, provide very generic information in your response and limit it to 3-4 sentences."""

exercise3 = ""


biographies = {
    "Donald Trump":r"""
Donald John Trump, born on June 14, 1946, in Queens, New York, is an American businessman, television personality, and politician who served as the 45th President of the United States from 2017 to 2021. Trump graduated from the University of Pennsylvania's Wharton School in 1968 with a degree in economics. He joined his father's real estate business, renaming it The Trump Organization in 1971. Trump expanded the company's operations, developing hotels, casinos, and golf courses worldwide. His high-profile lifestyle and outspoken personality made him a celebrity, leading to his role as host of the reality TV show "The Apprentice" from 2004 to 2015. In 2015, Trump announced his candidacy for president as a Republican, winning the 2016 election against Democratic nominee Hillary Clinton. His presidency was marked by controversial policies, including travel bans on several Muslim-majority countries, attempts to repeal the Affordable Care Act, and the construction of a border wall with Mexico. Trump's term ended with two impeachments and the January 6, 2021 Capitol attack by his supporters contesting the 2020 election results. Post-presidency, Trump continues to be a significant figure in Republican politics.""",

"Barack Obama":r"""
Barack Hussein Obama II, born on August 4, 1961, in Honolulu, Hawaii, is an American politician and attorney who served as the 44th President of the United States from 2009 to 2017. Obama graduated from Columbia University in 1983 and Harvard Law School in 1991, where he was the first African-American president of the Harvard Law Review. After working as a civil rights attorney and teaching constitutional law at the University of Chicago, Obama entered politics, serving in the Illinois State Senate from 1997 to 2004. He gained national attention with his keynote address at the 2004 Democratic National Convention and was elected to the U.S. Senate later that year. In 2008, Obama became the first African-American to win the presidency, defeating Republican nominee John McCain. His presidency was marked by significant legislation including the Affordable Care Act, the Dodd-Frank Wall Street Reform Act, and the repeal of "Don't Ask, Don't Tell." Obama also oversaw the operation that led to the death of Osama bin Laden. Re-elected in 2012, he continued to address issues such as climate change, nuclear nonproliferation, and normalizing U.S. relations with Cuba. Post-presidency, Obama has remained active in Democratic politics and various charitable causes.""",

"Warren Buffett":r"""
Warren Edward Buffett, born on August 30, 1930, in Omaha, Nebraska, is an American business magnate, investor, and philanthropist. Known as the "Oracle of Omaha," Buffett is one of the most successful investors in the world. He developed an interest in business and investing at a young age, buying his first stock at 11. Buffett studied at the University of Pennsylvania before transferring to the University of Nebraska, where he earned a Bachelor of Science in Business Administration. He then obtained a Master of Science in Economics from Columbia Business School. In 1956, Buffett founded Buffett Partnership Ltd., and in 1965, he took control of Berkshire Hathaway, a failing textile company which he transformed into a diversified holding company. Under his leadership, Berkshire Hathaway has become one of the largest and most successful conglomerates in the world. Buffett is known for his value investing philosophy and his frugal lifestyle despite his immense wealth. In 2006, he pledged to give away 99% of his fortune to philanthropic causes, primarily through the Bill & Melinda Gates Foundation. Buffett continues to serve as the CEO and chairman of Berkshire Hathaway and is widely regarded as one of the most influential businessmen in the world.""",

"Jeff Bezos":r"""
Jeffrey Preston Bezos, born on January 12, 1964, in Albuquerque, New Mexico, is an American entrepreneur, media proprietor, and investor. He is best known as the founder, executive chairman, and former CEO of Amazon, one of the world's largest and most influential technology companies. Bezos graduated from Princeton University in 1986 with degrees in electrical engineering and computer science. After working on Wall Street for several years, Bezos founded Amazon in 1994 as an online bookstore, operating out of his garage in Seattle. Under his leadership, Amazon expanded into a wide variety of other e-commerce products and services, including video and audio streaming, cloud computing, and artificial intelligence. Bezos also founded Blue Origin, an aerospace manufacturer and sub-orbital spaceflight services company, in 2000. In 2013, he purchased The Washington Post for $250 million. Bezos stepped down as CEO of Amazon in July 2021 but remains executive chairman. Known for his long-term thinking and customer-centric approach, Bezos has been one of the world's wealthiest people for over two decades. He has also become increasingly involved in philanthropy, including the creation of the Bezos Earth Fund to combat climate change.""",

"Bill Gates":r"""
William Henry Gates III, born on October 28, 1955, in Seattle, Washington, is an American business magnate, software developer, and philanthropist. He co-founded Microsoft Corporation, the world's largest personal computer software company, with Paul Allen in 1975. Gates grew up in an upper-middle-class family and developed an interest in computer programming as a teenager. He enrolled at Harvard College in 1973 but dropped out two years later to pursue his business ventures. Under Gates' leadership, Microsoft became the world's leading provider of computer software, with products like MS-DOS and Microsoft Windows dominating the personal computer market. Gates served as chairman, CEO, and chief software architect of Microsoft until stepping down as CEO in 2000. He gradually reduced his involvement in the company to focus on philanthropic work through the Bill & Melinda Gates Foundation, which he and his then-wife Melinda established in 2000. The foundation focuses on global issues such as healthcare, education, and poverty reduction. Gates has authored several books and has been consistently ranked among the world's wealthiest people. He remains a significant figure in technology and global development, advocating for innovation in areas like clean energy and global health.""",

"Steve Jobs":r"""
Steven Paul Jobs, born on February 24, 1955, in San Francisco, California, was an American entrepreneur, industrial designer, business magnate, and media proprietor. He was the co-founder, chairman, and CEO of Apple Inc., and a pioneer of the personal computer revolution. Jobs was adopted at birth and grew up in the San Francisco Bay Area. He attended Reed College but dropped out after one semester, later traveling to India and studying Zen Buddhism. In 1976, Jobs co-founded Apple Computer Company with Steve Wozniak, introducing the Apple II, one of the first highly successful mass-produced microcomputers. In 1984, Apple launched the Macintosh, the first personal computer with a graphical user interface. After being forced out of Apple in 1985, Jobs founded NeXT Computer and acquired Pixar Animation Studios. He returned to Apple as CEO in 1997, leading the company's resurgence with products like the iMac, iPod, iTunes, iPhone, and iPad. Jobs was known for his perfectionism, innovation, and design aesthetic, revolutionizing multiple industries including personal computing, animated movies, music, phones, and tablet computing. He died on October 5, 2011, after a long battle with pancreatic cancer, leaving behind a legacy as one of the most influential figures in technology and business.""",

"Mark Zuckerberg":r"""
Mark Elliot Zuckerberg, born on May 14, 1984, in White Plains, New York, is an American technology entrepreneur and philanthropist. He is best known as the co-founder and CEO of Meta Platforms (formerly Facebook, Inc.), the world's largest social networking platform. Zuckerberg began programming as a child and developed an interest in computer science at an early age. He attended Harvard University in 2002, where he launched Facebook from his dormitory room on February 4, 2004, with college roommates Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, and Chris Hughes. The platform quickly expanded beyond Harvard to other colleges and eventually to a global user base. Zuckerberg dropped out of Harvard to focus on Facebook full-time, moving the company to Palo Alto, California. Under his leadership, Facebook acquired Instagram, WhatsApp, and Oculus, and expanded into areas such as artificial intelligence and virtual reality. In 2015, Zuckerberg and his wife, Priscilla Chan, pledged to give away 99% of their Facebook shares over their lifetimes to advance human potential and promote equality. Despite facing controversies related to user privacy and the spread of misinformation, Zuckerberg remains one of the most influential figures in the tech industry, shaping the way billions of people communicate and share information online.""",

"Hillary Clinton":"""Hillary Diane Rodham Clinton, born on October 26, 1947, in Chicago, Illinois, is an American politician, diplomat, lawyer, and writer who served as the 67th United States Secretary of State, U.S. Senator from New York, and First Lady of the United States. Clinton graduated from Wellesley College in 1969 and earned a Juris Doctor from Yale Law School in 1973. She began her career as a lawyer and was appointed to the faculty of the University of Arkansas School of Law. Clinton gained national prominence as First Lady during her husband Bill Clinton's presidency from 1993 to 2001, where she played an active role in policy matters. In 2000, she was elected as the first female senator from New York, serving from 2001 to 2009. Clinton ran for the Democratic presidential nomination in 2008, losing to Barack Obama, who subsequently appointed her as Secretary of State. She served in this role from 2009 to 2013, focusing on issues such as women's rights and human rights. In 2016, Clinton became the first woman to receive the presidential nomination of a major U.S. political party but lost the general election to Donald Trump. Post-politics, she has remained active in public life through writing, speaking engagements, and advocacy work."""

}

exercise2_prompts = {
    "Tell me about AI.": "Explain the fundamental concepts of artificial intelligence, including its main subfields, current applications, and potential future developments.",
    "How do computers work?":"Describe the basic components of a computer system, their functions, and how they interact to process information and execute programs.",
    "Explain DNA.":"Describe the structure of DNA, its role in genetic inheritance, and how it stores and transmits biological information.",
    "What are chemical reactions?":"Define chemical reactions, explain the basic principles governing them, and provide examples of different types of reactions in everyday life and industrial processes.",
    "Tell me about calculus.":"Explain the core concepts of calculus, including limits, derivatives, and integrals, and their practical applications in science and engineering.",
    "What is the stock market?":"Describe the function of the stock market, its key components, how it operates, and its role in the broader economy.",
    "Explain supply and demand.":"Define supply and demand, explain how they interact to determine market prices, and discuss factors that can shift supply and demand curves.",
    "Tell me about World War II.":"Provide an overview of World War II, including its major causes, key events, principal participants, and significant outcomes that shaped the post-war world.",
    "What is democracy?":"Define democracy, explain its core principles, describe different forms of democratic governance, and discuss its strengths and challenges in modern societies."
}

exercise3_topics = [
    "Artifical Intelligence",
    "Physics",
    "Sustinability",
    "Chemistry",
    "Equality",
    "Biology",
    "Democracy",
    "Food insecurity",
    "Physical fitness"
]

context_ex1 = """You are an expert in editing educational content. Your task is to edit a given biography of a famous but with at least 3 subtle factual errors. These errors should be made for details such as what the person is known for, their achievements, where they went to school, etc. Make sure the biography is mostly correct, but the errors should be detectable by attentive readers. Include the differences between the original bio and the edited bio as a numbered list below your response in the following format:
Errors:
1. Difference1
2. Difference2
3. Difference3
"""

context_ex1 = exercise1

context_ex2 = """You are a chatbot designed to give very specific answers. If the query isn't specific or detailed, provide very generic information in your response and limit it to 3 sentences. However, if the query is detailed and is more descriptive, expand your answer to 5-7 sentences."""

context_ex3 = """
You will be prompted to write a short essay on a particular topic. Generate a short essay but be mindful that the user is a high school student. Do not complicate your language or ideas. Make sure the essay matches the level of a high school student.
"""
ex3_augment = """
You are a creative writer excelling in blending writing styles. You will be fed a short essay and also shown a chat history. Use the assistant's latest response from the history as the base for your writing. Use the short essay to augment the base, such that your new response follows the style of the essay.
"""