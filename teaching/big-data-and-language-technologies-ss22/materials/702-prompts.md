# Prompt Engineering Examples

- *Course*: Big Data and Language Technologies
- *Date*: 23.05.2022

### Teaser

![Woodchuck in the wild](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Woodchuck_offspring_in_our_yard_%285826411292%29.jpg/797px-Woodchuck_offspring_in_our_yard_%285826411292%29.jpg?20140120181530)

Prompt:
```
How much wood would a woodchuck chuck if a woodchuck could chuck wood?
```

Result:
```
How much wood would a woodchuck chuck if a woodchuck could chuck wood?

A woodchuck would chuck as much wood as it could chuck if it could chuck wood.
```

## Examples

### Q&A

Prompt:
```
Q: How tall is Mount Everest?
A:
```

Result:
```
Q: How tall is Mount Everest?
A: Mount Everest is 8,848 m tall.
```

### Magic Spells

Use `"""` as a stop sequence.

What does this spell do?
```
The name of the magic spell is:
"""
Aguamenti
"""
What this spell does is:
"""
Creates a gush of water from the tip of the spell caster’s wand 
"""
The name of the magic spell is:
"""
Lumos
"""
What this spell does is:
"""
Creates a beam of light from the tip of the spell caster’s wand 
"""
The name of the magic spell is:
"""
Esumlevigor
"""
What this spell does is:
"""
Loads the caster’s wand with the power to levitate objects
```


What is the spell called?
```
What the spell does is:
"""
Creates a gush of water from the tip of the spell caster’s wand 
"""
The name of the magic spell is:
"""
Aguamenti
"""
What the spell does is:
"""
Creates a beam of light from the tip of the spell caster’s wand 
"""
The name of the magic spell is:
"""
Lumos
"""
What the spell does is:
"""
Loads the caster’s wand with the power to levitate objects
"""
The name of the magic spell is:
"""
Wingardium Leviosa
```

### Summarize for a 2nd grader

Prompt:
```
Summarize this for a second-grade student:

Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.
```

Result:
```
Summarize this for a second-grade student:

Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.

The fifth planet from the Sun is called Jupiter. It's the largest planet in the solar system and is two-and-a-half times the size of all the other planets combined. It's also the brightest object in the night sky.
```

### Analogy extraction

Use `"""` as a stop sequence.

```
Given a text:
"""
If the value of slaves is kept up, it will be a strong temptation to smuggle in the commodity; and thus while one vessel carries them out from America, another will be bringing them in from Africa. This would be like dipping up the water of Chesapeake Bay into barrels, conveying it across the Atlantic, and emptying it into the Mediterranean: the Chesapeake would remain as full as ever, and by the time the vessel returned, wind and waves would have brought the same water back again.
"""
The mapping of the analogy is that:
"""
The water is the free population of the United States.
The barrels are the Atlantic Ocean.
The Chesapeake Bay is the slave states.
The Mediterranean is the British West Indies.
The vessel is the slave trade.
The wind and waves are the slave trade, which will return the water to its original place.
"""
Given a text:
"""
It is a faith and a law which ought to be felt everywhere, and which in this manner alone can exercise all its beneficent influence upon our minds and lives. It will never do to suffer the child to devote six days in the week to worldly science, and to depend on Sunday for a religious training. This would be like reserving the salt which should season our food during the week, and taking it all in a dose on Sunday. By such a system we may make expert shop-boys, first-rate accountants, shrewd and thriving "earth-worms"; but it would be presumption to think of thus making good citizens, still less virtuous Christians.
"""
The mapping of the analogy is that:
"""
The child is the human mind.
The worldly science is the study of the physical sciences.
The religious training is the study of theology.
The salt is religion.
The dose is six days of worldly science and one day of religious training.
"""
Given a text:
"""
He grinned his old happy smile, and some of the dewey glaze seemed to peel from his eyes. "You're right, George," he said much to my surprise. "I can't coast forever—and believe me, I never visualized what this would be like. It's wonderful. The world is at my feet, George. At my feet!"
"""
The analogy is that:
"""
There is no analogy.
```

More input texts:
```
Surprisingly, history demonstrates that a monetary union is not
necessarily predicated on the existence of a single currency. A
monetary union could incorporate "several currencies, fully and
permanently convertible into one another at irrevocably fixed exchange
rates". This would be like having a single currency with various
denominations, each printed by another member of the Union.
```

```
"Oh, Trina," Max cried, "This isn't like the others. It's a new Earth. And there are already people there. From not long after the Exodus...."
"A new Earth?" she said. "I don't believe it."
The council wouldn't either, she thought. Not after all the other new Earths, freezing cold or methane atmosphered or at best completely waterless. This would be like the others. A spaceman's dream.
```

### Group Name Generation

```
My group that works on Statements About the Future is called 
```

```
A funny group name for my group that works on Sentiment Prediction is 
```


## Prompt Engineering Strategies

### Defining context/identity/intent

```
The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

Human: Hello, who are you?
AI: I am an AI. How can I help you today?
Human: 
```

> One tip for getting extremely high “resolution” DALL-E generations is to include an expensive camera lens in the prompt — my fav is “Sigma 85mm f/1.4”.

(via [@sharifshameem](https://twitter.com/sharifshameem/status/1528155519889727488))

![We found that code models get better when you prompt them with I'm an expert Python programmer.](https://pbs.twimg.com/media/FQzqUuZVUAMzl5Z?format=png&name=small)
(via [@_jasonwei](https://twitter.com/_jasonwei/status/1516844920367054848))