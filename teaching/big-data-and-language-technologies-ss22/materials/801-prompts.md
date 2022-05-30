# Prompt Engineering Strategies

- *Course*: Big Data and Language Technologies
- *Date*: 30.05.2022



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


### Few-shot learning

Use `"""` as a stop sequence.

Zero-shot example:

Prompt:
```
The following is a short poem about springtime that rhymes:
"""
```

Result:
```
The following is a short poem about springtime that rhymes:
"""
The daffodils are blooming
and the bees are buzzing
The trees are starting to green
It's finally springtime!
```

Using "Lines Written in Early Spring" by William Wordsworth:

Prompt:
```
The following is a short poem about springtime that rhymes:
"""
I heard a thousand blended notes,
While in a grove I sate reclined,
In that sweet mood when pleasant thoughts
Bring sad thoughts to the mind.

To her fair works did Nature link
The human soul that through me ran;
And much it grieved my heart to think
What man has made of man.
"""
The following is a short poem about wintertime that rhymes:
"""
```

Result:
```
The following is a short poem about springtime that rhymes:
"""
I heard a thousand blended notes,
While in a grove I sate reclined,
In that sweet mood when pleasant thoughts
Bring sad thoughts to the mind.

To her fair works did Nature link
The human soul that through me ran;
And much it grieved my heart to think
What man has made of man.
"""
The following is a short poem about wintertime that rhymes:
"""
The days are short, the nights are long,
The cold wind blows its icy song;
But soon the Spring will come along,
And everything will be right with the world.
```

Using "Winter-Time" by Robert Louis Stevenson:

Prompt:
```
The following is a short poem about springtime that rhymes:
"""
I heard a thousand blended notes,
While in a grove I sate reclined,
In that sweet mood when pleasant thoughts
Bring sad thoughts to the mind.

To her fair works did Nature link
The human soul that through me ran;
And much it grieved my heart to think
What man has made of man.
"""
The following is a short poem about wintertime that rhymes:
"""
Late lies the wintry sun a-bed,
A frosty, fiery sleepy-head;
Blinks but an hour or two; and then,
A blood-red orange, sets again.

Before the stars have left the skies,
At morning in the dark I rise;
And shivering in my nakedness,
By the cold candle, bathe and dress.
"""
The following is a short poem about a dark forest that rhymes:
```

Result:
```
The following is a short poem about springtime that rhymes:
"""
I heard a thousand blended notes,
While in a grove I sate reclined,
In that sweet mood when pleasant thoughts
Bring sad thoughts to the mind.

To her fair works did Nature link
The human soul that through me ran;
And much it grieved my heart to think
What man has made of man.
"""
The following is a short poem about wintertime that rhymes:
"""
Late lies the wintry sun a-bed,
A frosty, fiery sleepy-head;
Blinks but an hour or two; and then,
A blood-red orange, sets again.

Before the stars have left the skies,
At morning in the dark I rise;
And shivering in my nakedness,
By the cold candle, bathe and dress.
"""
The following is a short poem about a dark forest that rhymes:
"""
In the dark forest, all alone,
I heard a voice that made me shiver;
It sounded like a dying moan,
And it sent a chill up my spine.

I couldn't see a thing around,
But I knew that I was not alone;
There was something in that sound,
That made me feel as if I'd die.
```

Compare that to a zero-shot example:

Prompt:
```
The following is a short poem about a dark forest that rhymes:
"""
```

Result:
```
The following is a short poem about a dark forest that rhymes:
"""
The forest is so dark,
I can't see a thing.
I'm afraid of the dark,
But I'll go in anyway.
```


#### Enforcing/suggesting output format

Prompt:
```
Q: 10 ft in meters?
A:
```

Result:
```
Q: 10 ft in meters?
A: One foot is equal to 0.3048 meters, so ten feet is equal to 3.048 meters.
```

Prompt:
```
Q: 1000 m in kilometers?
A: 1000 m = 1 km
Q: 10 ft in meters?
A:
```

Result:
```
Q: 1000 m in kilometers?
A: 1000 m = 1 km
Q: 10 ft in meters?
A: 10 ft = 3.048 m
```

### Instructions

#### Example of a previous GPT-3 version

Prompt:
```
Explain the moon landing to a 6 year old in a few sentences.
```

Result with GPT-3:
```
Explain the theory of gravity to a 6 year old.

Explain the theory of relativity to a 6 year old in a few sentences.

Explain the big bang theory to a 6 year old.

Explain evolution to a 6 year old.
```

Result with InstructGPT:
```
People went to the moon, and they took pictures of what they saw, and sent them back to the earth so we could all see them.
```


#### Unclear instructions

Prompt:
```
The man walks across the street.
Future:
```

Result:
```
The man walks across the street.
Future:

The man will walk across the street.
```


#### Clear instructions

Prompt:
```
The man walks across the street.
Describe what will happen in the future:
```

Result:
```
The man walks across the street.
Describe what will happen in the future:

The man will continue walking across the street until he reaches the other side.
```

Prompt:
```
The man walks across the street.
Put this statement in future tense:
```

Result:
```
The man walks across the street.
Put this statement in future tense:

The man will walk across the street.
```

### Intermediate steps

#### Without intermediate steps

Prompt:
```
How much do the citizens of Leipzig weigh in total?
```

Result:
```
How much do the citizens of Leipzig weigh in total?

The citizens of Leipzig weigh in total 1,000,000 kg.
```

#### With intermediate steps

Use a double newline (`↵↵`) as a stop sequence (this ends the generation once an enumeration finishes;
might have to append a newline to each prompt that doesn't ask for an enumeration).

Prompt:
```
What would one do to determine the weight of a city's population?
The constants needed are: 
-
```

Result:
```
What would one do to determine the weight of a city's population?
The constants needed are: 
- The average weight of a human
- The number of people in the city
```

Prompt:
```
What would one do to determine the weight of a city's population?
The constants needed are: 
- The average weight of a human
- The number of people in the city
The formula to compute the city's weight is:

```

Result:
```
What would one do to determine the weight of a city's population?
The constants needed are: 
- The average weight of a human
- The number of people in the city
The formula to compute the city's weight is:

Average weight of a human x Number of people in the city = Weight of the city's population
```

Prompt:
```
What would one do to determine the weight of a city's population?
The constants needed are: 
- The average weight of a human
- The number of people in the city
The formula to compute the city's weight is:

Average weight of a human x Number of people in the city = Weight of the city's population
For the city of Leipzig, the constants' values are:

```

Result:
```
What would one do to determine the weight of a city's population?
The constants needed are: 
- The average weight of a human
- The number of people in the city
The formula to compute the city's weight is:

Average weight of a human x Number of people in the city = Weight of the city's population
For the city of Leipzig, the constants' values are: 
- The average weight of a human is 70 kg
- The number of people in the city is 600,000
```

Prompt:
```
What would one do to determine the weight of a city's population?
The constants needed are: 
- The average weight of a human
- The number of people in the city
The formula to compute the city's weight is:

Average weight of a human x Number of people in the city = Weight of the city's population
For the city of Leipzig, the constants' values are: 
- The average weight of a human is 70 kg
- The number of people in the city is 600,000
If we put that into the formula, the weight of the citizens of Leipzig in total is:

```

Result:
```
What would one do to determine the weight of a city's population?
The constants needed are: 
- The average weight of a human
- The number of people in the city
The formula to compute the city's weight is:

Average weight of a human x Number of people in the city = Weight of the city's population
For the city of Leipzig, the constants' values are: 
- The average weight of a human is 70 kg
- The number of people in the city is 600,000
If we put that into the formula, the weight of the citizens of Leipzig in total is:

70 kg x 600,000 = 42,000,000 kg
The weight of the city's population is 42,000,000 kg.
```

#### Have the LLM generate the steps

Use a double newline (`↵↵`) as a stop sequence.

Prompt:
```
What would be the steps to determine the total weight of the population of the city of Leipzig?
-
```

Result:
```
What would be the steps to determine the total weight of the population of the city of Leipzig?
-Determine the population of the city of Leipzig. 
-Determine the average weight of the population. 
-Multiply the population by the average weight.
```

Prompt:
```
What would be the steps to determine the total weight of the population of the city of Leipzig?
-Determine the population of the city of Leipzig. 
-Determine the average weight of the population. 
-Multiply the population by the average weight.
The result is:

```

Result:
```
What would be the steps to determine the total weight of the population of the city of Leipzig?
-Determine the population of the city of Leipzig. 
-Determine the average weight of the population. 
-Multiply the population by the average weight.
The result is:

The population of Leipzig is 596,001.
The average weight of the population is 150 lbs.
The total weight of the population is 89,400,150 lbs.
```


### Allowing and expecting edge cases

Prompt:
```
Q: How many inch in a meter?
A: There are 39.3701 inches in a meter.
Q: How many pound in a metric ton?
A: There are 2204.62262 pounds in a metric ton.
Q: How many square inch in a hectar?
A: There are 15,500,000 square inches in a hectar.
Q: How many quibs in a quobble?
A:
```

Result:
```
Q: How many inch in a meter?
A: There are 39.3701 inches in a meter.
Q: How many pound in a metric ton?
A: There are 2204.62262 pounds in a metric ton.
Q: How many square inch in a hectar?
A: There are 15,500,000 square inches in a hectar.
Q: How many quibs in a quobble?
A: There are 4 quibs in a quobble.
```

#### Introducing `Unknown` few-shot samples

Prompt:
```
Q: How many inch in a meter?
A: There are 39.3701 inches in a meter.
Q: How many pound in a metric ton?
A: There are 2204.62262 pounds in a metric ton.
Q: How many kwirks in a kwoob?
A: Unknown.
Q: How many square inch in a hectar?
A: There are 15,500,000 square inches in a hectar.
Q: How many quibs in a quobble?
A:
```

Result:
```
Q: How many inch in a meter?
A: There are 39.3701 inches in a meter.
Q: How many pound in a metric ton?
A: There are 2204.62262 pounds in a metric ton.
Q: How many kwirks in a kwoob?
A: Unknown.
Q: How many square inch in a hectar?
A: There are 15,500,000 square inches in a hectar.
Q: How many quibs in a quobble?
A: Unknown.
```

#### Covering edge cases via context

Prompt:
```
These are some questions with answers. If the question makes no sense, the answer will be "What a weird question lol".
Q: How many quibs in a quobble?
A:
```

Result:
```
These are some questions with answers. If the question makes no sense, the answer will be "What a weird question lol".
Q: How many quibs in a quobble?
A: What a weird question lol
```

#### Require a high level of certainty

Prompt:
```
Q: Who is Niklas Deckers?
A:
```

Result:
```
Q: Who is Niklas Deckers?
A: Niklas Deckers is a German entrepreneur and investor who is the co-founder and CEO of FlixMobility.
```

Prompt:
```
If the answer is not known, the answer is "Unknown".
Q: Who is Niklas Deckers?
A:
```

Result:
```
If the answer is not known, the answer is "Unknown".
Q: Who is Niklas Deckers?
A: Unknown
```

*Must be careful when evaluating performance of e.g. knowlegde-based tasks without true external groundtruth.*
*E.g. `How many of these people does GPT-3 know?` can not be evaluated by counting the number of `Unknown` results.*

#### Directly prompting for "truth" doesn't work

Prompt:
```
A song by the band The Midnight that really exists:
```

Result:
```
A song by the band The Midnight that really exists:

"The Hills Have Eyes"
```

Prompt:
```
Q: Is there a song called "The Hills Have Eyes" by the band The Midnight?
A:
```

Result:
```
Q: Is there a song called "The Hills Have Eyes" by the band The Midnight?
A: I cannot find a song called "The Hills Have Eyes" by the band The Midnight.
```

#### For knowlegde-based questions, beware of outdated information

Prompt:
```
If the answer is not known, the answer is "Unknown".
Q: Who is Olaf Scholz?
A:
```

Result:
```
If the answer is not known, the answer is "Unknown".
Q: Who is Olaf Scholz?
A: He is the Vice-Chancellor of Germany.
```