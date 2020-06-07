message = ''' A society is a group of individuals involved in persistent social interaction, or a large social group sharing the same spatial or social territory, typically subject to the same political authority and dominant cultural expectations. Societies are characterized by patterns of relationships (social relations) between individuals who share a distinctive culture and institutions; a given society may be described as the sum total of such relationships among its constituent of members. In the social sciences, a larger society often exhibits stratification or dominance patterns in subgroups.

Societies construct patterns of behavior by deeming certain actions or speech as acceptable or unacceptable. These patterns of behavior within a given society are known as societal norms. Societies, and their norms, undergo gradual and perpetual changes.

Insofar as it is collaborative, a society can enable its members to benefit in ways that would otherwise be difficult on an individual basis; both individual and social (common) benefits can thus be distinguished, or in many cases found to overlap. A society can also consist of like-minded people governed by their own norms and values within a dominant, larger society. This is sometimes referred to as a subculture, a term used extensively within criminology.

More broadly, and especially within structuralist thought, a society may be illustrated as an economic, social, industrial or cultural infrastructure, made up of, yet distinct from, a varied collection of individuals. In this regard society can mean the objective relationships people have with the material world and with other people, rather than "other people" beyond the individual and their familiar social environment. '''

freq = {}

for letters in message:
	freq.setdefault(letters , 0)
	freq[letters] += 1 

import pprint	#prettyprint
pprint.pprint(freq)
