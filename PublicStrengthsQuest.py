import cgi
#allows get requests
import requests
#convert string into dictionary
import ast
#key for Thesaurus service provided by words.bighugelabs.com
key = ""

strengths = [
	{
		"name": "Achiever",
		"search": "Achieve",
		"type": "verb"
	},
	{
		"name": "Activator",
		"search": "Activate",
		"type": "verb"
	},
	{
		"name": "Adaptability",
		"search": "Adapt",
		"type": "verb"
	},
	{
		"name": "Analytical",
		"search": "Analyze",
		"type": "verb"
	},
	{
		"name": "Arranger",
		"search": "Arrange",
		"type": "verb"
	},
	{
		"name": "Belief",
		"search": "Belief",
		"type": "noun"
	},
	{
		"name": "Command",
		"search": "Command",
		"type": "verb"
	},
	{
		"name": "Communication",
		"search": "Communicate",
		"type": "verb"
	},
	{
		"name": "Competition",
		"search": "Compete",
		"type": "verb"
	},
	{
		"name": "Connectedness",
		"search": "Connect",
		"type": "verb"
	},
	{
		"name": "Consistency",
		"search": "Consistent",
		"type": "adjective"
	},
	{
		"name": "Context",
		"search": "Context",
		"type": "noun"
	},
	{
		"name": "Deliberative",
		"search": "Deliberate",
		"type": "verb"
	},
	{
		"name": "Developer",
		"search": "Develop",
		"type": "verb"
	},
	{
		"name": "Discipline",
		"search": "Discipline",
		"type": "noun"
	},
	{
		"name": "Empathy",
		"search": "Empathy",
		"type": "noun"
	},
	{
		"name": "Focus",
		"search": "Focus",
		"type": "verb"
	},
	{
		"name": "Futuristic",
		"search": "Futuristic",
		"type": "adjective"
	},
	{
		"name": "Harmony",
		"search": "Harmony",
		"type": "noun"
	},
	{
		"name": "Ideation",
		"search": "Ideation",
		"type": "noun"
	},
	{
		"name": "Includer",
		"search": "Include",
		"type": "verb"
	},
	{
		"name": "Individualization",
		"search": "Individual",
		"type": "adjective"
	},
	{
		"name": "Input",
		"search": "Input",
		"type": "noun"
	},
	{
		"name": "Intellection",
		"search": "Intellect",
		"type": "noun"
	},
	{
		"name": "Learner",
		"search": "Learn",
		"type": "verb"
	},
	{
		"name": "Maximizer",
		"search": "Maximize",
		"type": "verb"
	},
	{
		"name": "Positivity",
		"search": "Positivity",
		"type": "noun"
	},
	{
		"name": "Relator",
		"search": "Relate",
		"type": "verb"
	},
	{
		"name": "Responsibility",
		"search": "Responsibility",
		"type": "noun"
	},
	{
		"name": "Restorative",
		"search": "Restore",
		"type": "verb"
	},
	{
		"name": "Self-Assurance",
		"search": "Self-assurance",
		"type": "noun"
	},
	{
		"name": "Significance",
		"search": "Significance",
		"type": "noun"
	},
	{
		"name": "Strategic",
		"search": "Strategic",
		"type": "adjective"
	},
	{
		"name": "Woo",
		"search": "Woo",
		"type": "verb"
	}
]

user = input("Please give us your job description: ")
print("LOADING...")
for x in range(len(strengths)):
	#word that is searched for
	word = strengths[x]['search']
	wordType = strengths[x]['type']
	counter = 0
	#url that api calls
	url = 'http://words.bighugelabs.com/api/2/' + key + '/'+ word +'/json'
	#raw response
	response = requests.get(url)
	#raw content as a byte literal
	data = response.content
	#turn content into string
	stringData = data.decode("UTF-8")
	#turn content into dictionary 
	dictionary = ast.literal_eval(stringData)
	#list of synonyms
	synonyms = dictionary[wordType]['syn']
	
	#for every value in synonyms
	for num in range(len(synonyms)):
		current = synonyms[num]
		#if the current synonym is included in the job description add one to the counter
		if current in user:
			counter += 1
	if not (counter == 0):
		print(strengths[x]['name'])
		print(counter)		