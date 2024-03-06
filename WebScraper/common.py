import subprocess

# Define the command to run the Node.js file
mathplanet_links = ["node", "mathplanet_links.js"]
mathplanet_subsections = ["node", "mathplanet_subsections.js"]
mathplanet_content = ["node", "mathplanet_content.js"]
mathsisfun_content = ["node", "mathsisfun_content.js"]
oxnotes_links = ["node", "oxnotes_links.js"]
oxnotes_content = ["node", "oxnotes_content.js"]
paul_links = ["node", "paul_links.js"]
paul_content = ["node", "paul_content.js"]
oxnotes_subsections = ["node", "oxnotes_subsections.js"]
summarizer = ["node", "../Summarizer/code.js"]

# Run the Node.js file using subprocess
while True:
    print("1 - Math Planet\n2 - Maths Is Fun\n3 - Oxnotes\n4 - Paul's Online Notes\n5 - Summarize\n6 - Quit")
    option = int(input("What website do you want to go to?:  "))

    if option == 1:
        try:
            subprocess.run(mathplanet_links, check=True)
            print("Node.js file executed successfully")
        except subprocess.CalledProcessError as e:
            print("Error occurred while executing Node.js file:", e)
    if option == 2:
        try:
            subprocess.run(mathsisfun_content, check=True)
            print("Node.js file executed successfully")
        except subprocess.CalledProcessError as e:
            print("Error occurred while executing Node.js file:", e)
    if option == 3:
        try:
            subprocess.run(oxnotes_links, check=True)
            print("Node.js file executed successfully")
        except subprocess.CalledProcessError as e:
            print("Error occurred while executing Node.js file:", e)
    if option == 4:
        try:
            subprocess.run(paul_links, check=True)
            print("Node.js file executed successfully")
        except subprocess.CalledProcessError as e:
            print("Error occurred while executing Node.js file:", e)
    if option == 5:
        try:
            subprocess.run(summarizer, check=True)
            print("Node.js file executed successfully")
        except subprocess.CalledProcessError as e:
            print("Error occurred while executing Node.js file:", e)
    if option == 6:
        break

