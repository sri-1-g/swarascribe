import streamlit as st
raags = [
  {
    'name': 'Kanakangi',
    'arohana': 'S R₁ G₁ M₁ P D₁ N₁ S',
    'avarohana': 'S N₁ D₁ P M₁ G₁ R₁ S',
    'time_of_day': 'Early Morning',
    'character': 'Kanakangi conveys purity, simplicity, and devotion, often evoking a serene and meditative mood. The use of Shuddha Rishabham (R₁) and Shuddha Gandharam (G₁) creates a soft and delicate tonal quality, making the raga sound gentle yet profound.',
    'associated_deity_emotion': 'This raga is associated with Lord Vishnu and is believed to invoke tranquility, divine grace, and deep introspection. It is often linked to themes of devotion and prayer, making it a preferred choice for temple and early morning performances.',
    'musical_structure': 'Kanakangi follows the basic Sampurna scale structure without any vakra (zig-zag) patterns or special gamakas. Its notes are placed in their natural order, making it an essential raga for understanding the foundation of Carnatic melody.',
    'popular_compositions': [
      'Rama Nannu Brovara - Tyagaraja',
      'Sri Vighneswaraya - Muthuswami Dikshitar'
    ],
    'history': 'Kanakangi was classified as the first Melakarta raga by the musicologist Venkatamakhi in the 17th century and later reinforced by Govindacharya in the Katapayadi system. Although it is not widely used in compositions, its theoretical significance is immense, as it serves as a model for other ragas. Many later ragas borrow swaras from Kanakangi to create derived (janya) ragas.',
    'cultural_significance': 'Kanakangi is highly respected as a fundamental raga in Carnatic music. While it is not commonly used in performances, its pure and unornamented scale makes it a key raga for students learning the Melakarta system. It is also believed to have a calming effect on the mind, making it suitable for meditation and devotional music.'
  },
  {
  'name': 'Shanmukhapriya',
  'arohana': 'S R₁ G₁ M₁ P D₁ N₁ S',
  'avarohana': 'S N₁ D₁ P M₁ G₁ R₁ S',
  'time_of_day': 'Early Morning',
  'character': 'Shanmukhapriya evokes a mood of devotion, elegance, and grandeur, while also possessing a calming, meditative quality. The raga has a unique ability to blend both sweetness and strength, creating a profound emotional resonance. The use of Shuddha Rishabham (R₁), Shuddha Gandharam (G₁), and Shuddha Madhyamam (M₁) gives the raga its characteristic rich tonal color, while the notes D₁ and N₁ lend it a graceful yet commanding presence. It’s often described as a raga that soothes the mind while inspiring spiritual upliftment.',
  'associated_deity_emotion': 'Shanmukhapriya is associated with Lord Kartikeya (also known as Subrahmanya), the deity of war and youth. The raga is believed to evoke emotions of valor, purity, and devotion, and is said to invoke feelings of protection and divine grace. It is often used to connect the listener with themes of strength, peace, and reverence. This raga is frequently chosen for performances dedicated to Lord Subrahmanya, especially during early morning worship or in temple rituals that focus on invoking divine blessings.',
  'musical_structure': 'Shanmukhapriya follows the Sampurna scale with all seven notes in both the ascent and descent, without any vakra (zig-zag) movements. It is a straightforward, non-complicated raga, allowing for clear melodic progressions. The raga’s characteristic feature is the smooth usage of the notes, with emphasis on R₁, G₁, and M₁. The structure is devoid of any complex gamakas, but its richness comes from the natural flow of the notes and the steady pace of the raga. It is a quintessential raga for beginners to study as it gives a clear understanding of both the melodic and emotional framework of Carnatic music.',
  'popular_compositions': [
    'Shanmukhapriya - Muthuswami Dikshitar',
    'Subramanyaya Namah - Papanasam Sivan',
    'Shanmukhapriya Varnam - Kuppayah’
  ],
  'history': 'Shanmukhapriya is one of the 72 Melakarta ragas and was classified by the musicologist Venkatamakhi in his system of ragas. As the 6th Melakarta raga, it plays a significant role in the foundation of Carnatic music theory. Its melodic purity and emotional depth have made it an important raga in the early morning concert repertoire. Despite not being as widely popular in contemporary times, Shanmukhapriya remains a highly respected raga, especially for its association with devotional themes and its clear, unembellished melodic structure.',
  'cultural_significance': 'Shanmukhapriya holds a revered place in the Carnatic tradition, especially for its association with early morning concerts and devotional music. The raga is commonly performed in temple settings, often used to invoke the blessings of Lord Subrahmanya. Its pure melodic form and emotional balance make it a key raga for understanding the essence of Carnatic music and for students learning the Melakarta system. The soothing nature of Shanmukhapriya, combined with its devotional significance, makes it ideal for performances aimed at spiritual upliftment, prayer, and meditation. It is considered to have a calming influence, promoting peace and devotion among listeners.'
  },
  {
  'name': 'Ratnangi',
  'arohana': 'S R₂ G₁ M₁ P D₂ N₁ S',
  'avarohana': 'S N₁ D₂ P M₁ G₁ R₂ S',
  'time_of_day': 'Early Morning',
  'character': 'Ratnangi is a graceful and elegant raga, known for its smooth melodic flow and gentle optimism. The raga conveys a sense of beauty, tranquility, and refinement, making it ideal for expressions of devotion and admiration. The combination of Chatushruti Rishabham (R₂) and Chatushruti Dhaivatam (D₂) provides a lively yet sophisticated feel, while the use of Shuddha Gandharam (G₁), Shuddha Madhyamam (M₁), and Nishadam (N₁) brings balance and sweetness. Ratnangi evokes a mood that is uplifting and serene, perfect for morning renditions that are meant to soothe the mind and inspire devotion.',
  'associated_deity_emotion': 'Ratnangi is associated with Goddess Lakshmi, the deity of wealth, prosperity, and beauty. It is believed to evoke emotions of grace, beauty, spiritual wealth, and abundance. The raga is thought to invoke divine blessings, attracting harmony, prosperity, and well-being. It is particularly revered in temple rituals, where its gentle yet uplifting character complements prayers and invocations for divine grace. The serene mood of the raga is well-suited for early morning worship, creating an atmosphere of peace and devotion.',
  'musical_structure': 'Ratnangi follows a Sampurna scale, utilizing all seven notes (swaras) in both the ascent (arohana) and descent (avarohana) without vakra (zig-zag) or complex gamakas (ornamentations). The structure is smooth and straightforward, which contributes to its purity and accessibility. The clear progression of notes, along with the steady flow from R₂ to D₂, ensures that the raga maintains its melodic integrity while remaining expressive and open. Ratnangi’s lack of complex ornamentations makes it especially approachable for both beginner and advanced musicians. The raga’s simplicity is one of its defining features, allowing the performer to emphasize its inherent beauty and grace.',
  'popular_compositions': [
    'Sri Vighneswaraya - Muthuswami Dikshitar',
    'Rama Nannu Brovara - Tyagaraja (occasionally performed in certain interpretations)',
    'Venkatesa Suprabhatam - Prakasa',
    'Shri Lakshmi Narayana - Muthuswami Dikshitar'
  ],
  'history': 'Ratnangi was classified as the second Melakarta raga by the musicologist Venkatamakhi in his 17th-century raga classification system. It holds an important place in the Melakarta framework, though its presence in historical texts is more limited compared to other ragas. Its popularity grew in the 18th and 19th centuries with the rise of systematic raga codification. While Ratnangi is not as widely used in mainstream classical compositions, it remains integral to the study of Melakarta ragas, both for its theoretical importance and for its calming, devotional nature. Its role in morning concerts, especially in temple music, has further solidified its place in Carnatic music tradition.',
  'cultural_significance': 'Ratnangi is deeply rooted in the cultural and spiritual fabric of Carnatic music, especially in the context of temple music and early morning performances. The raga’s uplifting yet soothing quality makes it ideal for invoking devotion and seeking blessings during the early hours of the day, which are considered spiritually significant in Hinduism. It is a preferred raga for performances during morning rituals and religious gatherings, where its sweet, energetic, and positive vibrations are believed to bring about harmony, renewal, and prosperity. Ratnangi’s ability to balance sweetness with liveliness, alongside its association with Goddess Lakshmi, also makes it a symbol of divine grace and spiritual wealth.'
  },

  {
    'name': 'Shankarabharanam',
    'arohana': 'S R₂ G₃ M₁ P D₂ N₃ S',
    'avarohana': 'S N₃ D₂ P M₁ G₃ R₂ S',
    'time_of_day': 'Evening',
    'character': 'Shankarabharanam is uplifting, majestic, and grand. It conveys a sense of completeness, joy, and devotion, making it one of the most versatile ragas in Carnatic music.',
    'associated_deity_emotion': 'Associated with Lord Shiva, this raga is believed to evoke spiritual wisdom and cosmic harmony.',
    'musical_structure': 'This raga follows a completely linear scale and allows for extensive improvisation in both kalpana swaras and manodharma.',
    'popular_compositions': [
      'Endaro Mahanubhavulu - Tyagaraja',
      'Swara Raga Sudha - Tyagaraja'
    ],
    'history': 'One of the oldest and most fundamental ragas in Indian classical music, Shankarabharanam has been extensively used in both Carnatic and Hindustani traditions.',
    'cultural_significance': 'Shankarabharanam’s universal appeal makes it an essential raga in concerts and learning.'
  },
  {
  'name': 'Vanaspati',
  'arohana': 'S R₁ G₂ M₁ P D₁ N₂ S',
  'avarohana': 'S N₂ D₁ P M₁ G₂ R₁ S',
  'time_of_day': 'Late Morning',
  'character': 'Vanaspati carries a slightly introspective, emotional, and contemplative mood. It blends melancholy with hope, creating a balanced yet deep emotional landscape. The use of Shuddha Rishabham (R₁) and Shuddha Gandharam (G₂) provides the raga with a grounded, warm sound, while the inclusion of Shuddha Madhyamam (M₁) and the higher Nishadham (N₂) lends it a sense of yearning or introspection. The interplay between the notes gives Vanaspati a contemplative feel, evoking themes of change, renewal, and resilience. It’s a raga that invites reflection, making it ideal for performances that explore emotional depth and transformation.',
  'associated_deity_emotion': 'Vanaspati is associated with the natural world, symbolizing the growth of trees, the renewal of life, and the cycles of nature. It evokes emotions of change and transformation, often tied to the rejuvenation of life and the seasons. The raga is said to have a connection with Lord Vishnu in his form as a protector of nature and sustainer of life. It is believed to invoke feelings of reverence for nature, renewal, and the resilience of life. As such, Vanaspati is often performed in settings that emphasize natural beauty and spiritual growth, making it a suitable choice for both devotional and reflective themes.',
  'musical_structure': 'Vanaspati follows the Sampurna scale with all seven notes in both the ascending (arohana) and descending (avarohana) movements. It is a linear Melakarta raga with no vakra (zig-zag) patterns, meaning the notes move in a smooth, straight progression. The raga is known for its characteristic phrase combinations that define its uniqueness, particularly in the interplay between the notes R₁, G₂, D₁, and N₂, which creates a sense of continuity and flowing motion. Its structure gives it a calm, flowing character, suitable for both light and complex compositions. The smoothness of the raga’s progression allows performers to explore its emotional depth without the need for complex ornamentations, making it ideal for slow, reflective renditions.',
  'popular_compositions': [
    'Varashikivahana - Tyagaraja',
    'Sitamayi - Muthuswami Dikshitar',
    'Vanaspati Varnam - Kuppayah'
  ],
  'history': 'Vanaspati was classified as one of the Melakarta ragas by the musicologist Venkatamakhi in the 17th century. As the 47th Melakarta, it holds an important place in the system, though it is not as commonly performed in mainstream Carnatic concerts. Its melodic structure is straightforward and clear, yet its emotional complexity and thematic ties to nature and growth make it a unique raga within the Melakarta framework. While there is limited documentation on its historical usage, Vanaspati gained recognition over time for its evocative emotional range and subtle elegance. It continues to be respected for its theoretical importance in understanding the principles of Melakarta ragas.',
  'cultural_significance': 'Vanaspati, though rarely performed in contemporary concerts, carries significant cultural and theoretical weight in Carnatic music. It is a raga that represents nature’s cycles, especially the transitions between seasons, and invokes themes of growth, renewal, and change. The raga is traditionally associated with late morning performances, which further enhances its connection to the theme of renewal and the flourishing of life. Its melancholic yet hopeful nature makes it suitable for both classical compositions and lighter semi-classical forms. Despite being less frequently heard, Vanaspati is highly regarded by musicians and scholars for its distinct emotional depth and theoretical role in Carnatic music education.'
  },
  {
  'name': 'Manavati',
  'arohana': 'S R₁ G₂ M₁ P D₂ N₂ S',
  'avarohana': 'S N₂ D₂ P M₁ G₂ R₁ S',
  'time_of_day': 'Afternoon',
  'character': 'Manavati is a delicate yet intriguing raga, with a quiet depth that evokes curiosity and subtle emotional complexity. The combination of Shuddha Rishabham (R₁), Shuddha Gandharam (G₂), and the higher Nishadam (N₂) imparts an ethereal quality, while the use of Shuddha Madhyamam (M₁) and Chatushruti Dhaivatam (D₂) adds an element of richness and introspection. The raga’s understated nature creates an air of mystery and exploration, making it well-suited for compositions that delve into nuanced emotional expressions. While it carries a serene tone, it also has an underlying vibrancy that invites deeper listening and reflection.',
  'associated_deity_emotion': 'Manavati is associated with hidden wisdom, inner exploration, and mystical depth. It is believed to invoke emotions of mystery and introspection, often linked to the search for deeper truths and knowledge. This raga is thought to connect the listener with spiritual mysteries and the subtle, elusive aspects of existence. In some interpretations, it is associated with Lord Shiva in his form as the embodiment of wisdom and meditation, reinforcing its connection to contemplative thought and self-realization. Manavati’s emotional depth makes it ideal for evoking feelings of quiet contemplation and hidden understanding.',
  'musical_structure': 'Manavati follows the Sampurna scale, utilizing all seven notes in both the ascending (arohana) and descending (avarohana) movements. Its structure, however, allows for slight deviations in gamakas (ornamentations), which gives the raga its fluid, exploratory nature. The melodic progressions often weave through delicate note combinations, emphasizing smooth transitions rather than sharp contrasts. These subtle variations in gamakas contribute to its sense of mystery and refinement, making it a raga that can be interpreted in numerous ways depending on the artist’s approach. It offers a great deal of flexibility for expression, allowing performers to experiment with its emotional depth and hidden nuances.',
  'popular_compositions': [
    'Pahi Pahi Gajanana - Muthuswami Dikshitar',
    'Manavati Varnam - Kuppayyar',
    'Rama Nannu Brovara (in certain interpretations) - Tyagaraja'
  ],
  'history': 'Manavati, though not as widely known as other Melakarta ragas, holds a special place in the history of Carnatic music. Classified as the 39th Melakarta raga by Venkatamakhi, it has been part of the Melakarta system for centuries. Despite its relatively limited use in mainstream performances, it has been a significant raga for experimental compositions and scholarly pursuits. Manavati’s emotional range and flexibility have made it a favorite among composers looking for a raga that allows for nuanced interpretations and complex melodic structures. Its historical use, though not as widely documented, emphasizes its role in theoretical studies and explorations of raga form.',
  'cultural_significance': 'Although rarely performed in contemporary Carnatic music, Manavati carries substantial cultural and theoretical significance. The raga is often used in scholarly compositions and by musicians exploring the subtler, more experimental aspects of Carnatic music. Its flexible nature makes it an important tool for raga analysis and improvisation, particularly in academic and educational settings. The subtle emotional range and mysterious quality of Manavati make it suitable for performances that aim to explore deeper layers of expression. Its place in the Melakarta system ensures that it holds an important role in understanding the broader structure and theory of Carnatic music.'
  },

  {
    'name': 'Ganamurti',
    'arohana': 'S R₁ G₃ M₁ P D₁ N₁ S',
    'avarohana': 'S N₁ D₁ P M₁ G₃ R₁ S',
    'time_of_day': 'Early Morning',
    'character': 'Ganamurti carries an air of dignity and nobility, with a serious and contemplative tone. The presence of Antara Gandharam (G₃) and Shuddha Madhyamam (M₁) gives it a distinct blend of serenity and power. It is ideal for expressing reverence, devotion, and introspection, making it well-suited for spiritual or meditative compositions.',
    'associated_deity_emotion': 'Ganamurti is linked to Lord Ganesha, symbolizing wisdom, clarity, and the removal of obstacles. The raga evokes feelings of devotion, peace, and intellectual depth, often serving as an invocation for success and divine guidance.',
    'musical_structure': 'Ganamurti adheres to a structured Sampurna scale with a balanced arrangement of notes. The absence of vakra patterns gives it a straightforward and steady melodic progression, allowing for deep emotional exploration in both slow and medium-paced compositions.',
    'popular_compositions': [
      'Ganapati Bappa (popular devotional pieces)'
    ],
    'history': 'Ganamurti was formalized as the third Melakarta raga by Venkatamakhi and gained recognition in the early modern period. While it lacks an extensive historical record in ancient compositions, it became more prominent through its classification in the Melakarta system. The name "Ganamurthi" itself, meaning "embodiment of music," reflects its significance in Carnatic tradition. The raga was favored by Muthuswami Dikshitar for its structured, philosophical essence.',
    'cultural_significance': 'Ganamurti is closely associated with Lord Ganesha and is often performed at the beginning of concerts and religious ceremonies. Given its solemn and introspective nature, it is widely used in invocatory pieces and devotional music. The raga’s balance of depth and structure makes it an important choice for both classical performances and spiritual settings.'
  },
  {
    'name': 'Senavati',
    'arohana': 'S R₂ G₃ M₁ P D₂ N₁ S',
    'avarohana': 'S N₁ D₂ P M₁ G₃ R₂ S',
    'time_of_day': 'Late Morning to Early Afternoon',
    'character': 'Senavati conveys a feeling of serenity, balance, and subtle elegance. The use of Chatushruti Rishabham (R₂) and Chatushruti Dhaivatam (D₂) along with Antara Gandharam (G₃) brings out a majestic yet calm flavor, making it ideal for both reflective and grand expressions. It is a raga of moderate intensity, which allows for a range of emotional expressions from devotion to contemplation.',
    'associated_deity_emotion': 'Senavati is associated with Lord Shiva and is believed to evoke feelings of devotion, strength, and stability. It is often performed to invoke blessings for health, well-being, and inner peace.',
    'musical_structure': 'Senavati follows the Sampurna scale structure without any vakra (zig-zag) patterns. Its smooth melodic flow allows for both slow, meditative renditions as well as faster, more energetic compositions. The arrangement of notes is balanced and orderly, making it an essential raga for understanding the interrelations of notes in the Melakarta system.',
    'popular_compositions': [
      'Sree Ganeshwara - Muthuswami Dikshitar',
      'Senavathi Varnam - Unknown Composer'
    ],
    'history': 'Senavati was classified as the 59th Melakarta raga in the 72 Melakarta system by Venkatamakhi. While its use in ancient compositions is not as prominent as some other ragas, Senavati gained recognition in the 18th and 19th centuries, especially through its association with devotional and philosophical themes. The raga’s formal structure and balanced tone make it a staple in both classical and devotional music.',
    'cultural_significance': 'Senavati is widely regarded for its spiritual and emotional depth. It is often performed in temple settings, particularly during religious ceremonies and festivals. The raga’s association with Lord Shiva and its calm yet grand nature makes it a popular choice for invoking a sense of inner peace and spiritual connection during worship and meditation.'
 },
 {
  'name': 'Tanarupi',
  'arohana': 'S R₂ G₂ M₁ P D₂ N₁ S',
  'avarohana': 'S N₁ D₂ P M₁ G₂ R₂ S',
  'time_of_day': 'Late Evening',
  'character': 'Tanarupi conveys a mood of devotion and introspection, with a sense of calm and tranquility. The raga’s melodic structure, featuring the use of Shuddha Rishabham (R₂) and Shuddha Madhyamam (M₁), produces a sense of solemnity and reverence. The distinct use of Shuddha Dhaivatam (D₂) and Nishadham (N₁) further enhances the raga’s contemplative nature, making it both majestic and meditative. It evokes a serene, reflective atmosphere, making it ideal for evening renditions.',
  'associated_deity_emotion': 'Tanarupi is traditionally associated with Lord Shiva and is believed to invoke emotions of devotion, reverence, and deep introspection. It is said to connect the listener with the divine, promoting a heightened sense of spirituality and mindfulness. The raga is often chosen for performances during the late evening, a time that complements its reflective mood and invokes a sense of tranquility, ideal for spiritual gatherings and temple settings.',
  'musical_structure': 'Tanarupi follows the Sampurna scale, with seven notes in both the ascending (arohana) and descending (avarohana) movements. The raga’s structure is simple and direct, without any complex vakra (zigzag) patterns, making it easy to grasp for both novice and seasoned musicians. The notes R₂ and G₂, combined with M₁ and D₂, create a linear, flowing movement, maintaining clarity and purity in its execution. While there are no prominent gamakas (ornamentations) or intricate jantavari (note repetitions), the raga relies on smooth, straightforward execution of the notes, which enhances its meditative quality.',
  'popular_compositions': [
    'Tanarupiya - Muthuswami Dikshitar',
    'Shiva Shiva - Syama Sastri',
    'Rama Rama - Papanasam Sivan'
  ],
  'history': 'Tanarupi was classified as the 58th Melakarta raga by Venkatamakhi in the 17th century as part of the 72 Melakarta system. Despite its theoretical importance, it is not as widely used in contemporary Carnatic music as other Melakartas. Nevertheless, it is highly respected for its purity and simplicity, and it has inspired several janya ragas (derived ragas). While it is not frequently performed in concert halls, its serene nature makes it an essential raga for understanding the early evening mood and for training musicians in the subtlety of Melakarta ragas.',
  'cultural_significance': 'Tanarupi holds an esteemed position in Carnatic music due to its deep, meditative quality. It is particularly revered for its association with the late evening, a time often set aside for more introspective and devotional music. Though not commonly heard in performances, its place in the foundational study of Melakarta ragas is undeniable. The simplicity of its scale, combined with its deep emotional connection to Lord Shiva, makes it an important raga for meditation and spiritual reflection. It is believed to induce peace and contemplation, making it particularly suited for settings that call for devotion, prayer, and reflection, especially during temple and ritualistic music.'
 },

 {
    'name': 'Hanumatodi',
    'arohana': 'S R₁ G₂ M₁ P D₁ N₂ Ṡ',
    'avarohana': 'Ṡ N₂ D₁ P M₁ G₂ R₁ S',
    'time_of_day': 'Early Morning',
    'character': 'Hanumatodi is a powerful, devotional raga with a serious, bold character. It is known for its preference for lower notes, giving it a deep and gravitas-laden tone. The raga is full of emotional depth and is often associated with strength, courage, and reverence.',
    'associated_deity_emotion': 'Hanumatodi is associated with Lord Hanuman and is used to evoke feelings of strength, devotion, and protection. It is a raga that inspires reverence and deep devotion to the deity.',
    'popular_compositions': [
        'Era Na Pai - Patnam Subramania Iyer',
        'Thāye Yashoda - Oottukkadu Venkata Kavi',
        'Daani Samajendra - Swathi Thirunal',
        'Shri Krishnam Bhajamaanasa - Muthuswami Dikshitar',
        'Kādhanu vāriki - Thyagaraja',
        'Raave Himagiri Kumari - Syama Sastri'
    ],
    'history': 'Hanumatodi is the 8th melakarta raga in the 72 melakarta system, and it is a complex and challenging raga due to its intricate phrasing and intonation. It was classified by Venkatamakhi in the 17th century and has been used in several devotional compositions. The raga has a distinct connection to Lord Hanuman and has gained popularity in the Carnatic tradition over time, especially in the works of composers like Thyagaraja, Muthuswami Dikshitar, and Syama Sastri.',
    'cultural_significance': 'Hanumatodi, while not as widely performed as some other ragas, holds significant cultural value in Carnatic music, particularly in temple settings and devotional concerts. The raga is strongly associated with Lord Hanuman, symbolizing strength and protection, making it a popular choice for invoking blessings in devotional and spiritual contexts.'
},

{
    'name': 'Dhenuka',
    'arohana': 'S R₁ G₃ M₁ P D₁ N₁ S',
    'avarohana': 'S N₁ D₁ P M₁ G₃ R₁ S',
    'time_of_day': 'Night',
    'character': 'Dhenuka is a serene and meditative raga, known for its deep, contemplative nature. It creates a mood of calmness and solemnity, making it perfect for introspection and spiritual reflection. The combination of Shuddha Rishabham (R₁) and Antara Gandharam (G₃) gives it a soft yet profound tonal quality.',
    'associated_deity_emotion': 'Dhenuka is associated with Lord Shiva and is believed to evoke feelings of reverence, peace, and spiritual awareness. It is used to express devotion and introspection, invoking a sense of connection with the divine.',
    'popular_compositions': [
        'Dhenuka Varnam - Muthuswami Dikshitar'
    ],
    'history': 'Dhenuka is part of the Melakarta system and was classified by Venkatamakhi in the 17th century. It is considered one of the more peaceful ragas in the system, though its usage in compositions is not as widespread as some other ragas. The raga has a calming influence and is often chosen for slow, devotional pieces.',
    'cultural_significance': 'Dhenuka is a raga often associated with spiritual practices and is performed in temple settings or during devotional concerts. Its meditative quality makes it suitable for creating a tranquil atmosphere, and it is used to invoke a deep sense of peace and divine presence.'
},
{
    'name': 'Natakapriya',
    'arohana': 'S R₁ G₂ M₁ P D₂ N₂ S',
    'avarohana': 'S N₂ D₂ P M₁ G₂ R₁ S',
    'time_of_day': 'Morning',
    'character': 'Natakapriya is known for its dramatic and evocative quality, which makes it suitable for compositions that convey devotion or deep emotion. The combination of Shuddha Rishabham (R₁) and Sadharana Gandharam (G₂) gives it a somber yet soothing feel, while Chatusruti Dhaivatam (D₂) adds brightness to its overall character.',
    'associated_deity_emotion': 'Natakapriya is associated with Lord Vishnu and is believed to evoke feelings of devotion, peace, and reverence. It is often used to express divine connection and a sense of profound emotional depth in compositions.',
    'popular_compositions': [
        'Sri Venkatesa Girisam - Muthuswami Dikshitar',
        'Jagadeesha Guruguha - Muthuswami Dikshitar'
    ],
    'history': 'Natakapriya is part of the Melakarta system, classified by Venkatamakhin in the 17th century. It is one of the ragas used in both classical and devotional compositions. Although not as commonly performed as some other ragas, its emotional depth makes it highly revered in Carnatic music.',
    'cultural_significance': 'Natakapriya is often performed in temple settings and devotional concerts, where its dramatic and emotional qualities help to convey devotion and spiritual reverence. Its ability to evoke strong emotional connections makes it suitable for compositions in praise of deities, especially in the classical tradition.'
},
{
    'name': 'Bhairavi',
    'arohana': 'S R₁ G₃ M₁ P D₁ N₃ Ṡ',
    'avarohana': 'Ṡ N₃ D₁ P M₁ G₃ R₁ S',
    'time_of_day': 'Early Morning or Late Evening',
    'character': 'Bhairavi is associated with deep devotion, pathos, and longing. The use of Shuddha Madhyamam (M₁) and Shatsruti Rishabham (R₁) contributes to its somber and devotional feel. The raga evokes feelings of introspection, surrender, and melancholy, often performed in slow tempos to allow for deep emotional expression.',
    'associated_deity_emotion': 'Bhairavi is traditionally associated with intense devotion, spiritual release, and divine yearning. It expresses themes of separation and longing, often used in compositions to convey deep emotional connection with the divine.',
    'popular_compositions': [
        'Madhava Mamava - Muthuswami Dikshitar',
        'Bhavayami Gopalabalam - Annamacharya',
        'Enna Thavam Seithanai - Muthuswami Dikshitar',
        'Jagadananda Karaka - Tyagaraja',
        'Rama Nannu Brovara - Tyagaraja'
    ],
    'history': 'Bhairavi is an ancient raga, mentioned in early texts of Indian classical music, and has been a prominent part of both Carnatic and Hindustani music for centuries. In the Carnatic tradition, Bhairavi is a Melakarta raga and has long been used in devotional and classical music. It is believed to have deep cultural roots, originating from spiritual and devotional themes.',
    'cultural_significance': 'Bhairavi has significant cultural importance, especially in temple and devotional settings, where its emotional depth is used to evoke devotion and a connection to the divine. It plays a major role in classical concerts, especially during early morning or evening renditions, where its reflective and emotional qualities create a deeply meditative atmosphere.'
},
{
  "name": "Kalyani",
  "arohana": "S R₂ G₃ M₂ P D₂ N₃ Ṡ",
  "avarohana": "Ṡ N₃ D₂ P M₂ G₃ R₂ S",
  "time_of_day": "Evening",
  "character": "Kalyani is known for its regal and uplifting nature, with a combination of both brightness and depth. The use of Prati Madhyamam (M₂) and Antara Gandharam (G₃) imparts a sense of grandeur and elegance. The raga evokes feelings of devotion, serenity, and joy, often used to convey both the emotional depth and beauty of the divine.",
  "associated_deity_emotion": "Kalyani is associated with the Goddess Lakshmi and is believed to evoke feelings of devotion, grace, and prosperity. It is often used in compositions that express admiration, reverence, and the search for divine blessings.",
  "popular_compositions": [
    "Achyutam Keshavam - Annamacharya",
    "Jagadodharana - Purandara Dasa",
    "Kalyani Varnam - W. V. Srinivasa Ayyangar",
    "Sundara Viharini - Muthuswami Dikshitar"
  ],
  "history": "Kalyani is one of the most revered ragas in the Carnatic music tradition, often regarded as the quintessential raga for expressing devotion and grandeur. It is a melakarta raga and has been widely used in both classical compositions and performances, representing the culmination of emotional expression. Its origin dates back to the works of early composers like Muthuswami Dikshitar and Tyagaraja, who wrote some of their most popular pieces in this raga.",
  "cultural_significance": "Kalyani holds great cultural significance, particularly in classical Carnatic music and temple performances. Its ability to evoke feelings of beauty and reverence makes it a favorite in both light and classical music. It is performed in various settings, from concerts to festivals, symbolizing divine grace, wealth, and happiness."
},
{
  "name": "Kambhoji",
  "arohana": "S R₁ G₃ M₁ P D₁ N₃ Ṡ",
  "avarohana": "Ṡ N₃ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Night",
  "character": "Kambhoji is a majestic and grand raga, known for its deep, serious, and emotionally stirring character. The combination of Shuddha Rishabham (R₁) and Shuddha Madhyamam (M₁) with Kakali Nishadam (N₃) creates a raga of profound beauty and intensity. It evokes a sense of devotion, reverence, and intense emotion, often used to express the grandeur of divine presence.",
  "associated_deity_emotion": "Kambhoji is associated with Lord Shiva and is believed to evoke feelings of devotion, awe, and deep contemplation. It is often used in compositions dedicated to Lord Shiva, conveying a sense of grandeur, solemnity, and spiritual intensity.",
  "popular_compositions": [
    "Rama Nannu Brovara - Tyagaraja",
    "Bho Shambo - Muthuswami Dikshitar",
    "Vishnu Sahasranama Stotra - Muthuswami Dikshitar",
    "Dundubhi - Shyama Sastri"
  ],
  "history": "Kambhoji is one of the prominent ragas in Carnatic music and has been widely used by many legendary composers, including Tyagaraja, Muthuswami Dikshitar, and Shyama Sastri. It has a rich history and has been a central part of Carnatic music for centuries. The raga's profound emotional depth makes it a staple in both classical and devotional music.",
  "cultural_significance": "Kambhoji holds significant cultural importance in both the classical Carnatic music tradition and temple music. It is often performed during important religious ceremonies and festivals, especially in the evening and night. The raga's ability to convey intense emotion and reverence makes it a favorite in devotional concerts and spiritual gatherings."
},
{
  "name": "Kharaharapriya",
  "arohana": "S R₂ G₂ M₁ P D₂ N₂ Ṡ",
  "avarohana": "Ṡ N₂ D₂ P M₁ G₂ R₂ S",
  "time_of_day": "Late Evening",
  "character": "Kharaharapriya is a raga that exudes a feeling of devotion, serenity, and emotional intensity. The combination of Chatusruti Rishabham (R₂) and Sadharana Gandharam (G₂) gives it a smooth, contemplative quality, while Shuddha Madhyamam (M₁) and Kaisiki Nishadam (N₂) add richness to its sound. It is often used to express a sense of longing and deep emotional connection.",
  "associated_deity_emotion": "Kharaharapriya is associated with Lord Rama and is believed to evoke feelings of devotion, surrender, and reverence. It is often used in compositions that express the devotee's intense longing for the divine and their deep emotional connection with God.",
  "popular_compositions": [
    "Narayana Ninna Namada - Purandara Dasa",
    "Rama Ni Samanamevaru - Tyagaraja",
    "Kshamasva - Muthuswami Dikshitar"
  ],
  "history": "Kharaharapriya is a major melakarta raga that has inspired many compositions in the Carnatic tradition. Composers like Tyagaraja have written some of their most celebrated works in this raga. Its ability to convey deep emotional states makes it an enduring and beloved raga in the Carnatic music tradition.",
  "cultural_significance": "Kharaharapriya is widely performed in both classical concerts and devotional music. Its deep emotional resonance and ability to convey longing and introspection make it a favorite for expressing themes of devotion and spirituality. The raga is often performed in the later parts of classical concerts, providing a profound emotional impact."
},
{
    "name": "Todi",
    "arohana": "S R₁ G₃ M₁ P D₁ N₃ Ṡ",
    "avarohana": "Ṡ N₃ D₁ P M₁ G₃ R₁ S",
    "time_of_day": "Morning",
    "character": "Todi is an intense and serious raga, often used to convey devotion, longing, and introspection. Its deep and meditative tone is created by the use of Shuddha Rishabham (R₁) and Shuddha Dhaivatham (D₁).",
    "associated_deity_emotion": "Todi is associated with Lord Shiva and is believed to evoke feelings of reverence and spiritual yearning.",
    "popular_compositions": [
      "Kaddanu Variki - Tyagaraja",
      "Vathapi Ganapathim - Muthuswami Dikshitar",
      "Todi Varnam - Various composers"
    ],
    "history": "Todi is one of the oldest and most revered ragas in Carnatic music. It has been a favorite of composers like Tyagaraja and Dikshitar for its spiritual and emotional depth.",
    "cultural_significance": "Todi holds a prominent place in classical performances, symbolizing introspection and devotion. It is often used in compositions expressing longing and divine connection."
  },
  {
    "name": "Chakravakam",
    "arohana": "S R₁ G₃ M₁ P D₂ N₂ Ṡ",
    "avarohana": "Ṡ N₂ D₂ P M₁ G₃ R₁ S",
    "time_of_day": "Morning",
    "character": "Chakravakam is warm and soothing, evoking compassion and love. It is characterized by Chatusruti Dhaivatham (D₂) and Kaisiki Nishadam (N₂), creating a gentle and emotive sound.",
    "associated_deity_emotion": "Chakravakam is associated with Lord Surya, symbolizing vitality and gratitude.",
    "popular_compositions": [
      "Sugunamule - Tyagaraja",
      "Gajavadana - Papanasam Sivan"
    ],
    "history": "Chakravakam is the 16th melakarta raga and is loved for its emotional depth and simplicity. Its soothing nature has made it a preferred choice for both classical and devotional music.",
    "cultural_significance": "Chakravakam is frequently performed in devotional themes, emphasizing empathy and love."
  },
  {
    "name": "Mayamalavagowla",
    "arohana": "S R₁ G₃ M₁ P D₁ N₃ Ṡ",
    "avarohana": "Ṡ N₃ D₁ P M₁ G₃ R₁ S",
    "time_of_day": "Morning",
    "character": "Mayamalavagowla is serene and meditative, often taught as the foundational raga for beginners. Its symmetrical structure and tranquil tone make it ideal for learning swaras and basic compositions.",
    "associated_deity_emotion": "Mayamalavagowla is associated with Lord Ganesha, symbolizing clarity and auspicious beginnings.",
    "popular_compositions": [
      "Deva Deva Kalayami - Swathi Thirunal",
      "Meru Samana - Tyagaraja"
    ],
    "history": "Mayamalavagowla is the 15th melakarta raga and is a cornerstone of Carnatic music education. Its simplicity and emotional depth have inspired countless compositions.",
    "cultural_significance": "This raga plays a crucial role in music education and performances, symbolizing clarity and meditative focus."
  },
  {
  "name": "Kokilapriya",
  "arohana": "S R₃ G₃ M₁ P D₃ N₃ Ṡ",
  "avarohana": "Ṡ N₃ D₃ P M₁ G₃ R₃ S",
  "time_of_day": "Morning",
  "character": "Kokilapriya is a bright, cheerful, and playful raga, known for evoking feelings of joy and exuberance. Its lively character, coupled with the use of the higher notes like R₃, G₃, D₃, and N₃, gives it an energetic and uplifting quality. The raga creates an atmosphere of warmth and optimism, making it ideal for performances that aim to inspire happiness and lightheartedness. Kokilapriya is particularly noted for its bright tonal quality and its ability to elicit feelings of carefree joy. The interplay between its notes makes it a raga that invites both light, flowing melodies and rhythmic vitality, with a sense of youthful enthusiasm and celebration.",
  "associated_deity_emotion": "Kokilapriya is traditionally associated with Lord Krishna, whose life is often depicted as playful and filled with joyous moments, particularly with his flute. The raga symbolizes Krishna's playful devotion (bhakti) and his ability to bring happiness to his devotees. The energy of Kokilapriya is closely linked to the expressions of divine love, with the raga often evoking feelings of blissful devotion, celebration, and youthful energy. It mirrors the joy and carefree nature of Lord Krishna, and thus, it is commonly performed in settings that seek to invoke happiness, devotion, and playful energy.",
  "popular_compositions": [
    "Kokilamukha Nandasuta - Koteeswara Iyer",
    "Paripalaya Mam - Swathi Thirunal",
    "Rama Krishna Hari - Tyagaraja",
    "Krishna Ni Begane Baro - Mysore Vasudevachar"
  ],
  "history": "Kokilapriya is the 11th raga in the Melakarta system, classified by the musicologist Venkatamakhi in the 17th century. Although it is not one of the most frequently performed Melakartas, it holds a distinct identity for its bright and lively tone. The raga has been traditionally used in compositions that celebrate joy and happiness, often associated with Lord Krishna’s playful and carefree nature. Kokilapriya, with its emphasis on vivacity and liveliness, stands out for its unique ability to convey cheerfulness and devotion, although it is rarely used in mainstream Carnatic concerts compared to other Melakartas. Its role in the Melakarta system remains significant, as it offers insight into the emotional spectrum that can be conveyed through music.",
  "cultural_significance": "Kokilapriya is culturally significant in that it is often used in lighter, more playful performances. It is performed to evoke feelings of happiness, celebration, and playfulness, making it a popular choice for festive and thematic concerts. The raga is especially associated with devotional music centered around Lord Krishna, whose playful nature is mirrored in the raga’s lighthearted melodies. Kokilapriya’s cheerful disposition also makes it a suitable choice for compositions that depict divine love and devotion in a joyful context, often performed in temple settings or festive occasions. While it is not as commonly heard as some other Melakarta ragas, its bright, playful energy ensures its place in the rich tapestry of Carnatic music."
},


{
  'name': 'Rupavati',
  'arohana': 'S R₃ G₃ M₁ P D₁ N₁ S',
  'avarohana': 'S N₁ D₁ P M₁ G₃ R₃ S',
  'time_of_day': 'Evening',
  'character': 'Rupavati is a raga that exudes a calm and serene mood. Its structure gives it a contemplative quality, ideal for evoking a peaceful and meditative state. The subtle interplay of swaras creates an aura of tranquility, making it a perfect raga for reflective moments in the evening.',
  'associated_deity_emotion': 'Rupavati is associated with Goddess Saraswati, symbolizing wisdom, knowledge, and calm introspection. The raga inspires a deep sense of devotion, introspection, and a connection to learning and enlightenment.',
  'musical_structure': 'Rupavati follows the Sampurna scale structure with a combination of both major and minor intervals, creating a rich and delicate harmony. It is a classic example of a raga that fosters meditation, with smooth and deliberate transitions between notes.',
  'popular_compositions': [
    'Ganapathe Sugunatheetha - Koteeswara Iyer',
    'Sri Saraswathi - Muthuswami Dikshitar',
    'Rupavati Varnam - Subbaraya Sastry'
  ],
  'history': 'Rupavati is the 12th Melakarta raga in the 72 Melakarta system. Its serene and contemplative nature has made it a favored choice for devotional compositions and meditative performances. Though not as widely known as other Melakarta ragas, its gentle and introspective mood has earned it a niche following in both classical and devotional music.',
  'cultural_significance': 'Rupavati is often performed in temples and devotional settings, evoking feelings of gratitude, peace, and reverence. It is known for its role in expressing themes of devotion and introspection, especially in spiritual or meditative contexts.'
},
{
  'name': 'Vakulabharanam',
  'arohana': 'S R₁ G₃ M₁ P D₃ N₁ S',
  'avarohana': 'S N₁ D₃ P M₁ G₃ R₁ S',
  'time_of_day': 'Afternoon',
  'character': 'Vakulabharanam is a raga of dignity, grandeur, and solemnity. It conveys a mood of majesty and strength, invoking a sense of awe and reverence. The raga is known for its powerful and commanding character, making it ideal for compositions that express divine strength, protection, and triumph.',
  'associated_deity_emotion': 'Vakulabharanam is associated with Goddess Durga, symbolizing strength, power, and protection. It evokes feelings of courage and determination, often inspiring confidence and a sense of divine energy in the listener.',
  'musical_structure': 'Vakulabharanam is a Sampurna raga with a mix of natural and sharp notes, giving it a majestic and regal quality. The swara combinations bring out a deep sense of formality and grandeur, making it suitable for compositions that convey solemnity and strength.',
  'popular_compositions': [
    'Vakulabharanam Kriti - Tyagaraja',
    'Jagadamba Jagadamba - Muthuswami Dikshitar',
    'Sankari Sankuru - Shyama Shastri'
  ],
  'history': 'Vakulabharanam is the 14th Melakarta raga in the 72 Melakarta system. Its dignified and robust character has made it a favorite in both classical music and devotional compositions, particularly those focused on strength and divine protection.',
  'cultural_significance': 'Vakulabharanam is revered in Carnatic music for its bold and majestic nature. It is often performed in concerts to inspire respect, awe, and reverence. The raga is especially suited for invoking the power of Goddess Durga and is often used in the context of spiritual and devotional music.'
},
{
  'name': 'Gayakapriya',
  'arohana': 'S R₃ G₃ M₂ P D₁ N₁ S',
  'avarohana': 'S N₁ D₁ P M₂ G₃ R₃ S',
  'time_of_day': 'Morning',
  'character': 'Gayakapriya conveys a deep sense of devotion and introspection. It is known for its delicate balance between meditative calm and expressive beauty. The raga allows for intricate exploration, evoking a mood of reverence, peace, and spiritual connection in the listener.',
  'associated_deity_emotion': 'Gayakapriya is linked to Lord Vishnu, symbolizing divine grace, devotion, and gratitude. The raga creates an atmosphere of reverence and a strong emotional connection to the divine, making it ideal for prayers, offerings, and devotional music.',
  'musical_structure': 'Gayakapriya follows a Sampurna scale with a unique emphasis on the Prati Madhyamam (M₂), which sets it apart from other ragas. The smooth and expressive nature of the raga lends itself to both meditative exploration and lyrical expression, making it suitable for a range of devotional and reflective compositions.',
  'popular_compositions': [
    'Vandisuvudadiyali - Purandaradasa',
    'Sarasiruhasana Priye - Koteeswara Iyer',
    'Sri Venkateshwara - Thyagaraja'
  ],
  'history': 'Gayakapriya is the 13th Melakarta raga in the 72 Melakarta system. It is noted for its distinctive use of the Prati Madhyamam (M₂) which gives the raga its unique emotional flavor. Gayakapriya has captured the attention of both musicians and listeners, making it a revered raga in the Carnatic tradition.',
  'cultural_significance': 'Gayakapriya holds a special place in Carnatic music for its emotional depth and devotional quality. It is frequently performed during morning concerts, helping to create a serene and reflective ambiance. The raga is closely associated with the themes of devotion and connection to the divine, making it ideal for temple performances and devotional gatherings.'
},
{
  "name": "Suryakantam",
  "arohana": "S R₁ G₃ M₁ P D₂ N₃ S",
  "avarohana": "S N₃ D₂ P M₁ G₃ R₁ S",
  "time_of_day": "Morning",
  "character": "Suryakantam is a raga that radiates energy, brightness, and optimism. The combination of its notes brings out an uplifting and vibrant mood, often evoking feelings of renewal, hope, and vitality. The raga’s lively progression infuses a sense of warmth and positivity, making it ideal for the early hours of the day.",
  "associated_deity_emotion": "Suryakantam is associated with Lord Surya, the Sun God. It symbolizes vitality, life, and strength. The raga conveys feelings of gratitude and reverence for the Sun, which sustains life on Earth. Its lively nature is believed to evoke the divine energy and light associated with Surya.",
  "musical_structure": "Suryakantam is a Sampurna raga (seven notes in both ascent and descent). It follows a combination of Shuddha (natural) and sharp notes, particularly highlighting Rishabham (R₁) and Dhaivatam (D₂). The raga has a bright and open sound, with a distinct, optimistic feel due to the interplay of its swaras. The smooth transitions between the notes contribute to its dynamic and energetic quality.",
  "popular_compositions": [
    "Suryamurtim - Muthuswami Dikshitar",
    "Sri Saraswati Namostute - Koteeswara Iyer",
    "Suryakantam Varnam - Subbaraya Sastry"
  ],
  "history": "Suryakantam is the 17th melakarta raga in the 72 melakarta system. It is known for its bright, energetic nature, which has made it popular for compositions celebrating the Sun's energy. The raga’s role in early morning performances ties it to the renewal and vibrancy of the dawn.",
  "cultural_significance": "Suryakantam is revered for its ability to energize listeners, making it a popular choice for morning concerts. It is frequently performed in both devotional and classical settings, particularly at the start of the day, to invoke the strength and vitality associated with Lord Surya. The raga is known to inspire optimism and positivity."
},
{
  "name": "Hatakambari",
  "arohana": "S R₁ G₃ M₂ P D₂ N₃ S",
  "avarohana": "S N₃ D₂ P M₂ G₃ R₁ S",
  "time_of_day": "Afternoon",
  "character": "Hatakambari is a raga that embodies serenity, warmth, and grace. Its use of Prati Madhyamam (M₂) gives it a deep, meditative quality. The raga is soothing, evoking a sense of calm and introspection. It is ideal for compositions that emphasize tranquility and divine grace, making it a fitting choice for afternoon performances.",
  "associated_deity_emotion": "Hatakambari is linked to Goddess Lakshmi, the deity of wealth, prosperity, and benevolence. It is said to evoke feelings of peace, gratitude, and reverence, inspiring a connection to divine grace and abundance. The raga's gentle nature also aligns with Lakshmi's calming and nurturing qualities.",
  "musical_structure": "Hatakambari is a Sampurna raga, following the seven-note scale in both ascent and descent. The prominent use of M₂ adds a distinct warmth and softness to the raga, with its delicate and meditative character enhanced by the interplay of the swaras. It has a smooth and flowing quality, making it ideal for long, meditative phrases.",
  "popular_compositions": [
    "Hatakambari Varnam - Koteeswara Iyer",
    "Sri Lakshmi Stuti - Muthuswami Dikshitar",
    "Rama Raghukula - Tyagaraja"
  ],
  "history": "Hatakambari is the 18th melakarta raga in the 72 melakarta system. Known for its calming and introspective nature, it has been used for centuries in compositions that explore themes of divine grace and introspection. The raga is widely appreciated for its ability to create a peaceful and reflective atmosphere.",
  "cultural_significance": "Hatakambari is often performed in devotional settings, particularly those that seek to invoke peace, introspection, and divine blessings. Its association with Goddess Lakshmi makes it a favored raga during festivals and ceremonies that celebrate prosperity and well-being. It is highly valued in the Carnatic tradition for its meditative and soothing qualities."
},
{
  "name": "Jhankaradhwani",
  "arohana": "S R₂ G₃ M₁ P D₂ N₃ S",
  "avarohana": "S N₃ D₂ P M₁ G₃ R₂ S",
  "time_of_day": "Evening",
  "character": "Jhankaradhwani is a raga that exudes joy, vibrancy, and celebration. It is known for its lively and exuberant character, invoking feelings of festivity and divine playfulness. The raga has a distinctive rhythmic and melodic appeal, making it ideal for compositions that emphasize celebration and divine joy.",
  "associated_deity_emotion": "Jhankaradhwani is often associated with Lord Krishna, who represents divine playfulness and joy. The raga evokes a sense of bliss and carefree devotion, reflecting the playful and joyous nature of Krishna’s divine activities. It inspires an atmosphere of lightheartedness and joy.",
  "musical_structure": "Jhankaradhwani is a Sampurna raga, featuring seven notes in both the ascent and descent. It utilizes a combination of Shuddha (natural) and sharp notes, with R₂ (Chatusruti Rishabham) and D₂ (Chatusruti Dhaivatam) giving it a lively and bright character. The raga's structure allows for rhythmic complexity and melodic freedom, making it ideal for fast-paced and festive compositions.",
  "popular_compositions": [
    "Vande Vasudevam - Muthuswami Dikshitar",
    "Jhankaradhwani Tillana - Swathi Thirunal",
    "Jaya Jaya He - Tyagaraja"
  ],
  "history": "Jhankaradhwani is the 19th melakarta raga in the 72 melakarta system. Known for its joyful and celebratory nature, it has been a favorite choice for compositions that celebrate life, divine grace, and the festive spirit. The raga's vibrant character makes it suitable for both classical and light-hearted compositions.",
  "cultural_significance": "Jhankaradhwani is widely performed during festive occasions and in concerts that aim to create an atmosphere of celebration, joy, and devotion. It is particularly beloved for its ability to uplift the spirits and invoke divine bliss. The raga’s association with Lord Krishna makes it a common feature in celebrations dedicated to his divine exploits."
},
{
  "name": "Natabhairavi",
  "arohana": "S R₂ G₃ M₁ P D₁ N₂ S",
  "avarohana": "S N₂ D₁ P M₁ G₃ R₂ S",
  "time_of_day": "Afternoon",
  "character": "Natabhairavi is a raga that conveys a unique mix of solemnity, devotion, and emotional depth. Its structure evokes introspection and a sense of reverence, making it ideal for serious or devotional compositions. The raga’s intricate swara combinations highlight its emotional intensity, creating a mood that is both somber and devotional.",
  "associated_deity_emotion": "Natabhairavi is associated with Lord Shiva, the deity of destruction and transformation. It symbolizes strength, devotion, and inner resilience. The raga evokes deep feelings of reverence, and it is often performed to express spiritual yearning and the pursuit of enlightenment. It encourages a sense of surrender to the divine and acceptance of inner strength.",
  "musical_structure": "Natabhairavi is a Sampurna raga (seven notes in both ascent and descent), showcasing a combination of Shuddha (natural) and sharp notes. The use of R₂ (Chatusruti Rishabham) and D₁ (Shuddha Dhaivatam) adds gravity and intensity to the raga’s character. The flow from R₂ to M₁ and the subtle descent to S creates a contemplative atmosphere, ideal for exploring emotional depth.",
  "popular_compositions": [
    "Sri Venkatesa Girisham - Muthuswami Dikshitar",
    "Janani Mamava - Tyagaraja",
    "Enna Thavam Seithanai - Papanasam Sivan"
  ],
  "history": "Natabhairavi is the 20th melakarta raga in the 72 melakarta system. Its rich emotional landscape has made it a cornerstone of Carnatic music, frequently used for both classical and devotional compositions. The raga’s profound influence can be seen in its frequent use in compositions that express devotion and intense emotional experiences.",
  "cultural_significance": "Natabhairavi is considered one of the most emotional and versatile ragas in Carnatic music. It is often performed in both solo and group settings, and its ability to evoke deep emotions makes it a favorite for expressing themes of devotion, spiritual yearning, and introspection. The raga is also commonly used in temple music, enhancing its association with sacred rituals."
},
{
  "name": "Keeravani",
  "arohana": "S R₂ G₂ M₁ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₁ G₂ R₂ S",
  "time_of_day": "Evening",
  "character": "Keeravani is a raga known for its intense emotional depth and seriousness. It conveys a mood of melancholy, longing, and devotion, with its poignant swara combinations adding weight to its expression. The raga is perfect for compositions that explore complex emotions such as yearning, devotion, and reverence.",
  "associated_deity_emotion": "Keeravani is associated with Goddess Parvati, the divine mother and consort of Lord Shiva. She symbolizes maternal love, compassion, and nurturing. The raga evokes a deep emotional connection to the divine feminine, inspiring devotion and a longing for divine grace.",
  "musical_structure": "Keeravani follows a Sampurna scale with seven notes in both ascent and descent. The use of R₂ (Chatusruti Rishabham) and D₁ (Shuddha Dhaivatam) brings out the serious and somber character of the raga. The interplay between R₂ and G₂, along with the smooth descent to S, imparts a sense of melancholy, ideal for creating deep emotional resonance in compositions.",
  "popular_compositions": [
    "Kaligiyunte Kada - Tyagaraja",
    "Ambavani Nannu - Muthuswami Dikshitar",
    "Devi Neeye Thunai - Papanasam Sivan"
  ],
  "history": "Keeravani is the 21st melakarta raga in the 72 melakarta system. The raga’s distinctive emotional appeal, particularly its ability to convey longing and devotion, has made it a favorite among composers. It is often performed in the evening to evoke a deep sense of emotional connection and reflection.",
  "cultural_significance": "Keeravani is a highly regarded raga in Carnatic music, known for its profound emotional range. It is widely performed in both devotional and classical settings, where its ability to evoke intense feelings allows for deep musical exploration. Keeravani is particularly valued for its connection to the divine and its capacity to convey heartfelt emotions in music."
},
{
  "name": "Gourimanohari",
  "arohana": "S R₂ G₃ M₁ P D₂ N₂ S",
  "avarohana": "S N₂ D₂ P M₁ G₃ R₂ S",
  "time_of_day": "Morning",
  "character": "Gourimanohari is a raga known for its graceful, charming, and serene qualities. It exudes elegance and calm, making it suitable for compositions that are both melodious and devotional. The raga’s structure emphasizes a smooth flow of notes, creating an atmosphere of peace and reverence, ideal for morning performances.",
  "associated_deity_emotion": "Gourimanohari is associated with Goddess Durga, who embodies grace, power, and strength. The raga evokes feelings of devotion, tranquility, and calm reverence, inspiring a connection to the divine feminine. It emphasizes spiritual peace and devotion to the goddess, making it a suitable raga for invoking divine blessings.",
  "musical_structure": "Gourimanohari is a Sampurna raga with seven notes in both ascent and descent. It is characterized by the use of R₂ (Chatusruti Rishabham) and D₂ (Antara Dhaivatam), which add grace and elegance to the raga. The smooth transitions and balanced nature of the raga make it well-suited for devotional compositions and meditative explorations.",
  "popular_compositions": [
    "Rama Ninnu Namminanu - Tyagaraja",
    "Kamalambike - Muthuswami Dikshitar",
    "Gourimanohara - Papanasam Sivan"
  ],
  "history": "Gourimanohari is the 23rd melakarta raga in the 72 melakarta system. Its graceful and versatile nature has made it a favorite for composers, particularly in compositions that emphasize devotional themes. The raga’s melodic elegance has made it a key feature in both classical and devotional music.",
  "cultural_significance": "Gourimanohari is often performed in both devotional and concert settings. Its graceful character allows it to appeal to audiences while retaining a sense of classical depth. The raga is particularly revered for its ability to convey both devotion and serenity, making it suitable for invoking blessings from Goddess Durga and creating a peaceful atmosphere."
},
{
  "name": "Mararanjani",
  "arohana": "S R₂ G₃ M₂ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₂ G₃ R₂ S",
  "time_of_day": "Evening",
  "character": "Mararanjani is a raga that blends poignancy with elegance. Its distinctive use of Prati Madhyamam (M₂) creates a soft, ethereal quality, giving the raga a sense of emotional depth. It is ideal for compositions that explore complex emotional themes, invoking both introspection and devotional feelings.",
  "associated_deity_emotion": "Mararanjani is associated with Lord Krishna, who represents divine playfulness and compassion. The raga conveys the emotional depth of Krishna's divine love and playful nature, evoking feelings of devotion and longing. It is often linked to themes of divine grace and emotional connection with the deity.",
  "musical_structure": "Mararanjani is a Sampurna raga, utilizing seven notes in both ascent and descent. The use of M₂ (Prati Madhyamam) adds a unique tone, creating an ethereal and delicate feel. The raga’s structure allows for both fast-paced and meditative compositions, with its melancholic beauty being particularly suited to evening performances.",
  "popular_compositions": [
    "Mararanjani Tillana - Swathi Thirunal",
    "Mararanjani Varnam - Papanasam Sivan",
    "Govinda Gopala - Tyagaraja"
  ],
  "history": "Mararanjani is the 25th melakarta raga in the 72 melakarta system. It is known for its unique melodic structure, which blends emotional poignancy with elegance. This raga has become a favorite for compositions that explore deep feelings of devotion and longing, often performed in the evening.",
  "cultural_significance": "Mararanjani is appreciated for its ability to convey complex emotions. It is often performed in concerts and devotional settings, where its emotional depth allows the performer to connect with the audience on a profound level. The raga’s association with Lord Krishna makes it a popular choice for expressing divine love and devotion."
},
{
  "name": "Varunapriya",
  "arohana": "S R₂ G₃ M₁ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₁ G₃ R₂ S",
  "time_of_day": "Afternoon",
  "character": "Varunapriya is a raga that conveys a sense of calm and meditative introspection. Its structure is evocative and soothing, making it ideal for reflective compositions.",
  "associated_deity_emotion": "Varunapriya is associated with Lord Varuna, symbolizing water and serenity. It inspires feelings of calmness and inner peace.",
  "popular_compositions": [
    "Varunapriya Kriti - Koteeswara Iyer"
  ],
  "history": "Varunapriya is the 24th melakarta raga in the 72 melakarta system. Its tranquil quality has been appreciated for centuries, often being explored in meditative compositions.",
  "cultural_significance": "Varunapriya is valued for its reflective and calming nature. It is frequently performed in settings that focus on devotion and contemplation."
},
{
  "name": "Charukesi",
  "arohana": "S R₂ G₃ M₁ P D₁ N₂ S",
  "avarohana": "S N₂ D₁ P M₁ G₃ R₂ S",
  "time_of_day": "Evening",
  "character": "Charukesi is a raga known for its emotional depth and versatility. It conveys a mix of pathos and devotion, making it suitable for compositions that explore themes of love, devotion, and longing.",
  "associated_deity_emotion": "Charukesi is often associated with Goddess Saraswati, representing knowledge and devotion. It inspires feelings of spiritual yearning and emotional expression.",
  "popular_compositions": [
    "Adamodi Galade - Tyagaraja",
    "Kripaya Palaya - Muthuswami Dikshitar",
    "Charukesi Varnam - Lalgudi Jayaraman"
  ],
  "history": "Charukesi is the 26th melakarta raga in the 72 melakarta system. Its evocative and expressive nature has made it one of the most popular ragas in Carnatic music.",
  "cultural_significance": "Charukesi is widely performed in both classical and devotional settings. Its profound emotional appeal makes it a favorite among composers and audiences alike."
},
{
  "name": "Sarasangi",
  "arohana": "S R₂ G₃ M₁ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₁ G₃ R₂ S",
  "time_of_day": "Morning",
  "character": "Sarasangi is a raga with a bright and energetic quality. Its structure conveys positivity and enthusiasm, making it ideal for compositions that are lively and devotional.",
  "associated_deity_emotion": "Sarasangi is associated with Lord Vishnu, symbolizing protection and divine grace. It evokes feelings of joy and reverence.",
  "popular_compositions": [
    "Maravairi Ramani - Tyagaraja",
    "Sri Saraswati Namostute - Muthuswami Dikshitar"
  ],
  "history": "Sarasangi is the 27th melakarta raga in the 72 melakarta system. Its vibrant nature has been appreciated for centuries, particularly for its use in compositions praising deities.",
  "cultural_significance": "Sarasangi is frequently performed in classical and devotional concerts. Its energetic appeal makes it a versatile raga suitable for a variety of themes."
},
{
  "name": "Harikambhoji",
  "arohana": "S R₂ G₃ M₁ P D₂ N₂ S",
  "avarohana": "S N₂ D₂ P M₁ G₃ R₂ S",
  "time_of_day": "Afternoon",
  "character": "Harikambhoji is a raga that conveys a sense of balance and happiness. Its structure allows for both light and serious compositions, making it a versatile and popular raga.",
  "associated_deity_emotion": "Harikambhoji is associated with Lord Krishna, symbolizing joy and divine playfulness. It evokes feelings of happiness and devotion.",
  "popular_compositions": [
    "Dinamani Vamsa - Tyagaraja",
    "Rama Ninnu Namminanu - Tyagaraja",
    "Enduku Nirdaya - Tyagaraja"
  ],
  "history": "Harikambhoji is the 28th melakarta raga in the 72 melakarta system. Its versatility and cheerful nature have made it a cornerstone of Carnatic music.",
  "cultural_significance": "Harikambhoji is frequently performed in concerts due to its flexibility and audience appeal. It is often used in compositions that explore themes of devotion and joy."
},
{
  "name": "Shulini",
  "arohana": "S R₂ G₃ M₂ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₂ G₃ R₂ S",
  "time_of_day": "Evening",
  "character": "Shulini is a raga that exudes a calm and spiritual atmosphere. Its prati madhyamam lends it a tranquil and soothing quality, making it ideal for meditative compositions.",
  "associated_deity_emotion": "Shulini is associated with Goddess Durga, symbolizing strength and protection. It evokes feelings of calm confidence and devotion.",
  "popular_compositions": [
    "Jaya Jaya Padmanabha - Swathi Thirunal",
    "Parama Pavana Rama - Muthuswami Dikshitar"
  ],
  "history": "Shulini is the 35th melakarta raga in the 72 melakarta system. It is known for its serenity and the sense of balance it brings to compositions.",
  "cultural_significance": "Shulini is often performed in devotional settings, adding a sense of peace and introspection to the atmosphere."
},
{
  "name": "Chalanata",
  "arohana": "S R₁ G₃ M₁ P D₃ N₃ S",
  "avarohana": "S N₃ D₃ P M₁ G₃ R₁ S",
  "time_of_day": "Morning",
  "character": "Chalanata is a raga with a majestic and commanding presence. Its structure conveys a mix of grandeur and energy, making it suitable for bold compositions.",
  "associated_deity_emotion": "Chalanata is associated with Lord Vishnu, symbolizing sustenance and protection. It evokes feelings of strength and resilience.",
  "popular_compositions": [
    "Paripalaya Sarasiruha - Swathi Thirunal",
    "Gopala Iyer Kriti in Chalanata"
  ],
  "history": "Chalanata is the 36th melakarta raga in the 72 melakarta system. Its bold and vibrant character has made it a favorite for compositions that convey power and majesty.",
  "cultural_significance": "Chalanata is often performed in grand settings, bringing an aura of authority and confidence to classical concerts."
},
{
  "name": "Salagam",
  "arohana": "S R₁ G₃ M₁ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Evening",
  "character": "Salagam is a raga with a serene and meditative quality. Its structure evokes a sense of inner peace and spiritual depth.",
  "associated_deity_emotion": "Salagam is associated with Lord Shiva, symbolizing tranquility and devotion. It evokes feelings of introspection and surrender.",
  "popular_compositions": [
    "Salagatim - Thyagaraja"
  ],
  "history": "Salagam is the 37th melakarta raga in the 72 melakarta system. Its calm and introspective nature has made it a preferred choice for devotional compositions.",
  "cultural_significance": "Salagam is performed in settings that inspire devotion and inner peace, often used in compositions with spiritual themes."
},
{
  "name": "Jalarnavam",
  "arohana": "S R₁ G₃ M₂ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₂ G₃ R₁ S",
  "time_of_day": "Morning",
  "character": "Jalarnavam is a raga with a serene and refreshing character. Its prati madhyamam adds a unique and uplifting quality to its structure.",
  "associated_deity_emotion": "Jalarnavam is associated with Varuna, the deity of water, symbolizing purity and flow. It evokes feelings of renewal and devotion.",
  "popular_compositions": [
    "Sri Venkatesa Charanam - Thyagaraja"
  ],
  "history": "Jalarnavam is the 38th melakarta raga in the 72 melakarta system. Its uplifting and unique structure makes it a favorite for compositions with refreshing themes.",
  "cultural_significance": "Jalarnavam is performed in concerts that explore themes of nature and spirituality, bringing a sense of renewal to audiences."
},
{
  "name": "Jhalavarali",
  "arohana": "S R₁ G₃ M₂ P D₃ N₃ S",
  "avarohana": "S N₃ D₃ P M₂ G₃ R₁ S",
  "time_of_day": "Evening",
  "character": "Jhalavarali is a raga with a bold and dynamic character. Its prati madhyamam and sharp notes give it an energetic and commanding quality.",
  "associated_deity_emotion": "Jhalavarali is associated with Lord Rudra, symbolizing energy and power. It evokes feelings of strength and resilience.",
  "popular_compositions": [
    "Jhalavarali Kriti - Koteeswara Iyer"
  ],
  "history": "Jhalavarali is the 39th melakarta raga in the 72 melakarta system. Its bold nature has made it a favorite for compositions that convey intensity and vigor.",
  "cultural_significance": "Jhalavarali is often performed in powerful and energetic settings, adding a sense of drama to classical concerts."
},
{
  "name": "Navaneetam",
  "arohana": "S R₁ G₃ M₁ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Morning",
  "character": "Navaneetam is a raga with a sweet and melodious character. Its structure evokes a sense of simplicity and joy, often associated with playful and tender emotions.",
  "associated_deity_emotion": "Navaneetam is associated with Lord Krishna, symbolizing playfulness and charm. It evokes feelings of love and devotion.",
  "popular_compositions": [
    "Navaneetha Krishna - Annamacharya"
  ],
  "history": "Navaneetam is the 40th melakarta raga in the 72 melakarta system. Its sweet and melodious nature has made it a staple in devotional and playful compositions.",
  "cultural_significance": "Navaneetam is frequently performed in settings that highlight themes of love and devotion, particularly towards Lord Krishna."
},
{
  "name": "Naganandini",
  "arohana": "S R₁ G₃ M₂ P D₃ N₃ S",
  "avarohana": "S N₃ D₃ P M₂ G₃ R₁ S",
  "time_of_day": "Morning",
  "character": "Naganandini is a serene and meditative raga with a peaceful character. Its prati madhyamam provides a soothing quality, perfect for reflective compositions.",
  "associated_deity_emotion": "This raga is often associated with Lord Vishnu, symbolizing harmony and balance. It evokes feelings of tranquility and devotion.",
  "popular_compositions": [
    "Vishnu Vardhanane - Muthuswami Dikshitar",
    "Naganandini Pallavi - M. Balamuralikrishna"
  ],
  "history": "Naganandini is the 30th melakarta raga in the 72 melakarta system. It is a rare raga often performed to evoke a calm, reflective mood.",
  "cultural_significance": "This raga is appreciated for its tranquility and is frequently chosen for spiritual or meditative themes."
},
{
  "name": "Yagapriya",
  "arohana": "S R₃ G₃ M₁ P D₁ N₁ S",
  "avarohana": "S N₁ D₁ P M₁ G₃ R₃ S",
  "time_of_day": "Afternoon",
  "character": "Yagapriya is an uplifting raga that brings forth an atmosphere of devotion and energy. Its unique structure provides a bright and cheerful feel.",
  "associated_deity_emotion": "Yagapriya is associated with Agni, the god of fire, symbolizing purity and transformation.",
  "popular_compositions": [
    "Jaya Jaya Yagapriya - Swathi Thirunal",
    "Ganapathiye Karunanidhe - Periyasami Thooran"
  ],
  "history": "As the 31st melakarta raga, Yagapriya’s bright notes have inspired compositions filled with spiritual fervor and devotion.",
  "cultural_significance": "Yagapriya is often performed in energetic settings, symbolizing renewal and purity."
},
{
  "name": "Ragavardhini",
  "arohana": "S R₁ G₃ M₂ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₂ G₃ R₁ S",
  "time_of_day": "Evening",
  "character": "Ragavardhini is an introspective raga, known for its meditative and serene qualities. The prati madhyamam adds a layer of complexity and richness.",
  "associated_deity_emotion": "This raga is associated with Lord Shiva, evoking a sense of deep devotion and surrender.",
  "popular_compositions": [
    "Ragavardhini Pallavi - M. Balamuralikrishna",
    "Evarikai - Thyagaraja"
  ],
  "history": "Ragavardhini, the 32nd melakarta, is a lesser-known raga, valued for its contemplative mood and spiritual depth.",
  "cultural_significance": "It is often used in devotional settings, particularly in compositions exploring divine love and longing."
},
{
  "name": "Gangeyabhushani",
  "arohana": "S R₃ G₃ M₂ P D₃ N₃ S",
  "avarohana": "S N₃ D₃ P M₂ G₃ R₃ S",
  "time_of_day": "Morning",
  "character": "Gangeyabhushani has a bold and majestic tone. It conveys a sense of grandeur and depth, making it ideal for compositions of a royal or divine nature.",
  "associated_deity_emotion": "Associated with Goddess Ganga, it evokes feelings of purity and divinity.",
  "popular_compositions": [
    "Gangeyabhushani Varnam - Koteeswara Iyer",
    "Sri Gangeya Vasana - Muthuswami Dikshitar"
  ],
  "history": "Gangeyabhushani is the 33rd melakarta raga, known for its rich and striking character, often performed in royal or temple settings.",
  "cultural_significance": "This raga is a tribute to the Ganges, symbolizing purity and spiritual elevation."
},
{
  "name": "Vagadheeswari",
  "arohana": "S R₁ G₃ M₂ P D₃ N₃ S",
  "avarohana": "S N₃ D₃ P M₂ G₃ R₁ S",
  "time_of_day": "Evening",
  "character": "Vagadheeswari is a raga of deep and profound emotion. Its unique structure gives it a mystical and spiritual quality.",
  "associated_deity_emotion": "This raga is often linked with Goddess Saraswati, symbolizing wisdom and knowledge.",
  "popular_compositions": [
    "Paramatmudu Velige - Thyagaraja",
    "Sri Vagadheeswari - Muthuswami Dikshitar"
  ],
  "history": "Vagadheeswari is the 34th melakarta raga, revered for its meditative and introspective character. It has inspired many compositions that explore spiritual themes.",
  "cultural_significance": "It is commonly performed in settings that emphasize wisdom and devotion, often associated with Saraswati pooja celebrations."
},
{
  "name": "Pavani",
  "arohana": "S R₁ G₁ M₂ P D₁ N₁ S",
  "avarohana": "S N₁ D₁ P M₂ G₁ R₁ S",
  "time_of_day": "Morning",
  "character": "Pavani is a serene raga with a meditative and introspective mood. Its unique combination of notes makes it soothing and peaceful.",
  "associated_deity_emotion": "Pavani is associated with Lord Vishnu, symbolizing purity and tranquility.",
  "popular_compositions": [
    "Gananayakam Bhajeham - Muthuswami Dikshitar"
  ],
  "history": "Pavani is the 41st melakarta raga in the Carnatic music system. Its distinct structure lends itself to devotional compositions.",
  "cultural_significance": "This raga is particularly favored for meditative and spiritual renditions in temple music."
},
{
  "name": "Raghupriya",
  "arohana": "S R₁ G₂ M₂ P D₁ N₁ S",
  "avarohana": "S N₁ D₁ P M₂ G₂ R₁ S",
  "time_of_day": "Morning",
  "character": "Raghupriya is a bright and melodious raga with an uplifting character. It evokes a sense of joy and devotion.",
  "associated_deity_emotion": "This raga is associated with Lord Rama, symbolizing valor and virtue.",
  "popular_compositions": [
    "Siddhi Vinayakam - Muthuswami Dikshitar"
  ],
  "history": "Raghupriya, the 42nd melakarta raga, is known for its vibrant and auspicious nature, often used in compositions praising Lord Rama.",
  "cultural_significance": "It is widely performed in concert settings, particularly in kritis that narrate divine stories."
},
{
  "name": "Bhavapriya",
  "arohana": "S R₂ G₂ M₂ P D₁ N₂ S",
  "avarohana": "S N₂ D₁ P M₂ G₂ R₂ S",
  "time_of_day": "Morning",
  "character": "Bhavapriya is a deeply emotional raga, conveying a sense of devotion and introspection. Its melody has a gentle and calming appeal.",
  "associated_deity_emotion": "Bhavapriya is associated with Goddess Lakshmi, symbolizing grace and prosperity.",
  "popular_compositions": [
    "Sri Chamundeshwari Palayamam - Muthuswami Dikshitar"
  ],
  "history": "Bhavapriya, the 44th melakarta, is known for its deeply devotional and emotional content, making it a favorite among traditional musicians.",
  "cultural_significance": "It is commonly rendered in devotional and spiritual settings, with compositions focused on bhakti and reflection."
},
{
  "name": "Shubhapantuvarali",
  "arohana": "S R₁ G₂ M₂ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₂ G₂ R₁ S",
  "time_of_day": "Late Night",
  "character": "Shubhapantuvarali is a raga filled with pathos and intensity. It conveys deep emotions such as longing, devotion, and even despair.",
  "associated_deity_emotion": "This raga is often associated with Lord Shiva, symbolizing deep meditation and a connection to the cosmic.",
  "popular_compositions": [
    "Ennalu Urake - Thyagaraja",
    "Sri Satyanarayanam - Muthuswami Dikshitar"
  ],
  "history": "Shubhapantuvarali is the 45th melakarta raga and is revered for its emotional intensity and spiritual depth.",
  "cultural_significance": "This raga is popular in both classical concerts and devotional settings, especially for expressing intense emotions."
},
{
  "name": "Gavambhodi",
  "arohana": "S R₂ G₂ M₂ P D₁ N₁ S",
  "avarohana": "S N₁ D₁ P M₂ G₂ R₂ S",
  "time_of_day": "Evening",
  "character": "Gavambhodi is a rare raga with a contemplative and mysterious character. It is meditative and introspective.",
  "associated_deity_emotion": "This raga is often associated with Lord Shiva, evoking feelings of surrender and deep devotion.",
  "popular_compositions": [
    "Gavambhodi Krithi - Koteeswara Iyer"
  ],
  "history": "As the 43rd melakarta, Gavambhodi is a rarely performed raga, appreciated for its serene and mystical appeal.",
  "cultural_significance": "This raga is most often performed in devotional contexts or experimental compositions."
},
{
  "name": "Bhavapriya",
  "arohana": "S R₂ G₂ M₂ P D₁ N₂ S",
  "avarohana": "S N₂ D₁ P M₂ G₂ R₂ S",
  "time_of_day": "Morning",
  "character": "Bhavapriya is a deeply emotional raga, conveying a sense of devotion and introspection. Its melody has a gentle and calming appeal.",
  "associated_deity_emotion": "Bhavapriya is associated with Goddess Lakshmi, symbolizing grace and prosperity.",
  "popular_compositions": [
    "Bhavapriya Varnam - Koteeswara Iyer",
    "Sri Chamundeshwari Palayamam - Muthuswami Dikshitar"
  ],
  "history": "Bhavapriya, the 44th melakarta, is known for its deeply devotional and emotional content, making it a favorite among traditional musicians.",
  "cultural_significance": "It is commonly rendered in devotional and spiritual settings, with compositions focused on bhakti and reflection."
},
{
  "name": "Shadvidamargini",
  "arohana": "S R₂ G₁ M₂ P D₁ N₁ S",
  "avarohana": "S N₁ D₁ P M₂ G₁ R₂ S",
  "time_of_day": "Late Evening",
  "character": "Shadvidamargini is a raga that is known for its soothing, serene character, often evoking peaceful emotions.",
  "associated_deity_emotion": "This raga is associated with Lord Ganesha, symbolizing intellect and prosperity.",
  "popular_compositions": [
    "Shadvidamargini Varnam - Various Composers"
  ],
  "history": "Shadvidamargini is an uncommon raga in Carnatic music and is noted for its calm and serene appeal.",
  "cultural_significance": "Although rare, it is valued for performances in slow, meditative contexts."
},
{
  "name": "Suvarnangi",
  "arohana": "S R₁ G₃ M₂ P D₁ N₁ S",
  "avarohana": "S N₁ D₁ P M₂ G₃ R₁ S",
  "time_of_day": "Morning",
  "character": "Suvarnangi is a lively and bright raga that exudes warmth and radiance, often creating a festive and joyful atmosphere.",
  "associated_deity_emotion": "Suvarnangi is linked to Lord Vishnu, representing abundance and auspiciousness.",
  "popular_compositions": [
    "Suvarnangi Varnam - Koteeswara Iyer"
  ],
  "history": "Suvarnangi is a melakarta raga with a rich, melodious structure, commonly used in light and devotional compositions.",
  "cultural_significance": "This raga is especially used in celebratory and auspicious contexts in Carnatic music."
},
{
  "name": "Divyamani",
  "arohana": "S R₁ G₃ M₁ P D₁ N₂ S",
  "avarohana": "S N₂ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Evening",
  "character": "Divyamani is a raga that conveys a sense of devotion and peacefulness. It has a serene yet profound emotional depth.",
  "associated_deity_emotion": "This raga is associated with Lord Vishnu and is believed to invoke purity and spiritual awakening.",
  "popular_compositions": [
    "Divyamani Krithi - Muthuswami Dikshitar"
  ],
  "history": "Divyamani is a rare but significant raga, with its melodious structure often used for devotional purposes.",
  "cultural_significance": "This raga is particularly used in spiritual settings, where it is used to express purity and divine connection."
},
{
  "name": "Dhavalambari",
  "arohana": "S R₁ G₃ M₁ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Night",
  "character": "Dhavalambari is known for its elegance and grace, with a soft and soothing tonal quality that brings tranquility.",
  "associated_deity_emotion": "This raga is associated with Goddess Durga, symbolizing strength and protection.",
  "popular_compositions": [
    "Dhavalambari Varnam - Various Composers"
  ],
  "history": "Dhavalambari is a relatively rare raga in Carnatic music, celebrated for its subtle beauty.",
  "cultural_significance": "This raga is often used in performances that require delicate and intricate emotional expressions."
},
{
  "name": "Namanarayani",
  "arohana": "S R₂ G₂ M₂ P D₂ N₂ S",
  "avarohana": "S N₂ D₂ P M₂ G₂ R₂ S",
  "time_of_day": "Morning",
  "character": "Namanarayani is a raga that has a soulful and serene character, often invoking spiritual reflections.",
  "associated_deity_emotion": "This raga is associated with Lord Vishnu, symbolizing divinity and peace.",
  "popular_compositions": [
    "Namanarayani Varnam - Various Composers"
  ],
  "history": "Namanarayani is an uncommon raga that is typically used for slow, meditative compositions.",
  "cultural_significance": "This raga is performed in spiritual concerts and is used to express deep devotion and reverence."
},
{
  "name": "Ramapriya",
  "arohana": "S R₁ G₃ M₁ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Morning",
  "character": "Ramapriya is a raga that radiates warmth and affection, often evoking a sense of devotion and emotional depth.",
  "associated_deity_emotion": "This raga is associated with Lord Rama, symbolizing devotion, courage, and righteousness.",
  "popular_compositions": [
    "Sri Ramachandra Kripalu - Lalgudi Jayaraman",
    "Rama Nannu Brovara - Tyagaraja"
  ],
  "history": "Ramapriya is a beloved raga in the Carnatic tradition, known for its lyrical beauty and emotional depth, particularly in devotional contexts.",
  "cultural_significance": "This raga is frequently performed during spiritual and devotional concerts, especially to praise Lord Rama."
},
{
  "name": "Kamavardhini",
  "arohana": "S R₁ G₁ M₁ P D₁ N₂ S",
  "avarohana": "S N₂ D₁ P M₁ G₁ R₁ S",
  "time_of_day": "Night",
  "character": "Kamavardhini is a raga that conveys a feeling of longing and passion, often evoking romantic emotions.",
  "associated_deity_emotion": "This raga is associated with Lord Kama, symbolizing love and desire.",
  "popular_compositions": [
    "Kamavardhini Varnam - Various Composers"
  ],
  "history": "Kamavardhini is an emotional raga used in compositions that evoke longing or intense feeling.",
  "cultural_significance": "It is a popular raga for both romantic and devotional compositions."
},
{
  "name": "Gamanashrama",
  "arohana": "S R₁ G₃ M₁ P D₁ N₁ S",
  "avarohana": "S N₁ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Late Night",
  "character": "Gamanashrama is a peaceful raga that evokes a sense of tranquility and divine connection, often used for meditative purposes.",
  "associated_deity_emotion": "This raga is linked to Lord Shiva, symbolizing asceticism and deep meditation.",
  "popular_compositions": [
    "Gamanashrama Varnam - Various Composers"
  ],
  "history": "Gamanashrama is a rare but significant raga in the Carnatic tradition, typically used in slow and meditative compositions.",
  "cultural_significance": "Although not as commonly performed as other ragas, Gamanashrama holds importance in devotional and contemplative performances."
},
{
  "name": "Vishwambari",
  "arohana": "S R₁ G₃ M₁ P D₂ N₂ S",
  "avarohana": "S N₂ D₂ P M₁ G₃ R₁ S",
  "time_of_day": "Evening",
  "character": "Vishwambari is a raga that evokes a sense of grandeur and spiritual upliftment, conveying a message of hope and solace.",
  "associated_deity_emotion": "This raga is associated with Goddess Saraswati, symbolizing wisdom and learning.",
  "popular_compositions": [
    "Vishwambari Varnam - Various Composers",
    "Ganesha Pancharatnam - Muthuswami Dikshitar"
  ],
  "history": "Vishwambari is an ancient raga in the Carnatic tradition, often performed in concerts that celebrate learning and spirituality.",
  "cultural_significance": "This raga is commonly used in compositions dedicated to deities of wisdom and knowledge."
},
{
  "name": "Shamalangi",
  "arohana": "S R₂ G₂ M₂ P D₂ N₃ S",
  "avarohana": "S N₃ D₂ P M₂ G₂ R₂ S",
  "time_of_day": "Morning",
  "character": "Shamalangi is a graceful raga that invokes a sense of peace and divinity. Its melody is gentle, with an emotional depth that can inspire reverence.",
  "associated_deity_emotion": "This raga is associated with Goddess Durga, symbolizing power and purity.",
  "popular_compositions": [
    "Shamalangi Krithi - Muthuswami Dikshitar"
  ],
  "history": "Shamalangi is a raga that has been highly regarded in the Carnatic tradition, appreciated for its beautiful blend of harmony and emotion.",
  "cultural_significance": "This raga is performed during auspicious and spiritual events, evoking devotion and reflection."
},
{
  "name": "Simhendramadhyamam",
  "arohana": "S R₂ G₃ M₂ P D₁ N₂ S",
  "avarohana": "S N₂ D₁ P M₂ G₃ R₂ S",
  "time_of_day": "Morning",
  "character": "Simhendramadhyamam is a majestic raga, filled with a regal and uplifting tone that conveys both serenity and grandeur.",
  "associated_deity_emotion": "This raga is associated with Lord Indra, symbolizing power, wisdom, and the cosmic order.",
  "popular_compositions": [
    "Simhendramadhyamam Varnam - Various Composers",
    "Madhyamavathi - Muthuswami Dikshitar"
  ],
  "history": "Simhendramadhyamam is a powerful raga in the Carnatic tradition, often used to convey intense emotions and spiritual grandeur.",
  "cultural_significance": "This raga is particularly important in performances that aim to express awe and reverence, especially in devotional music."
},
{
  "name": "Hemavati",
  "arohana": "S R₂ G₃ M₁ P D₂ N₃ S",
  "avarohana": "S N₃ D₂ P M₁ G₃ R₂ S",
  "time_of_day": "Late Afternoon",
  "character": "Hemavati is a raga that evokes feelings of devotion and peacefulness, often conveying a sense of serenity and reflective calmness.",
  "associated_deity_emotion": "Hemavati is associated with Goddess Lakshmi, symbolizing wealth, prosperity, and spiritual serenity.",
  "popular_compositions": [
    "Hemavati Varnam - Various Composers",
    "Sri Lakshmi Narayana - Muthuswami Dikshitar"
  ],
  "history": "Hemavati is a well-established raga in Carnatic music, widely admired for its peaceful mood and often used in compositions centered around divine themes.",
  "cultural_significance": "This raga is performed in concerts to evoke peace and tranquility, especially in devotional settings."
},
{
  "name": "Dharmavati",
  "arohana": "S R₁ G₃ M₁ P D₂ N₂ S",
  "avarohana": "S N₂ D₂ P M₁ G₃ R₁ S",
  "time_of_day": "Night",
  "character": "Dharmavati is a raga known for its uplifting and profound emotional resonance, often reflecting a sense of reverence and spiritual integrity.",
  "associated_deity_emotion": "This raga is associated with the principle of Dharma, symbolizing moral order, virtue, and righteousness.",
  "popular_compositions": [
    "Dharmavati Varnam - Various Composers",
    "Rama Bhakti Samrajya - Tyagaraja"
  ],
  "history": "Dharmavati is a raga with a deep connection to spiritual themes, often used in compositions that reflect moral values and virtues.",
  "cultural_significance": "This raga is performed in the evening or night, often in spiritual and devotional contexts to promote moral and ethical introspection."
},
{
  "name": "Neetimati",
  "arohana": "S R₃ G₃ M₂ P D₃ N₃ S",
  "avarohana": "S N₃ D₃ P M₂ G₃ R₃ S",
  "time_of_day": "Morning",
  "character": "Neetimati is a bold and majestic raga, evoking energy, clarity, and strength. It conveys a mood of grandeur and inspiration.",
  "associated_deity_emotion": "Neetimati is often associated with Lord Vishnu, symbolizing protection and cosmic balance.",
  "popular_compositions": [
    "Sri Venkatesam Bhaje - Muthuswami Dikshitar",
    "Gananayakam Bhajeham - Koteeswara Iyer"
  ],
  "history": "Neetimati, the 60th melakarta, is known for its grandeur and is often used in compositions that emphasize clarity and strength.",
  "cultural_significance": "This raga is ideal for compositions focused on spiritual and devotional themes."
},
{
  "name": "Kantamani",
  "arohana": "S R₂ G₂ M₂ P D₃ N₃ S",
  "avarohana": "S N₃ D₃ P M₂ G₂ R₂ S",
  "time_of_day": "Evening",
  "character": "Kantamani is an intricate and delicate raga that evokes a sense of mystery and emotional depth. Its unique structure makes it melodically rich.",
  "associated_deity_emotion": "This raga is associated with Goddess Saraswati, representing wisdom and creativity.",
  "popular_compositions": [
    "Varavallabha Ramana - Muthuswami Dikshitar",
    "Saraseeruhasana Priye - Swati Tirunal"
  ],
  "history": "Kantamani is a rare melakarta raga, known for its serene and mystic quality, often used in intricate compositions.",
  "cultural_significance": "It is performed in both concerts and devotional settings to highlight its contemplative nature."
},
{
  "name": "Rishabhapriya",
  "arohana": "S R₃ G₃ M₂ P D₁ N₁ S",
  "avarohana": "S N₁ D₁ P M₂ G₃ R₃ S",
  "time_of_day": "Morning",
  "character": "Rishabhapriya is a vibrant raga, exuding strength and exuberance, while also carrying a meditative undertone.",
  "associated_deity_emotion": "This raga is linked to Lord Shiva, reflecting asceticism and cosmic energy.",
  "popular_compositions": [
    "Gopalaka Pahimam - Muthuswami Dikshitar"
  ],
  "history": "Rishabhapriya is a melakarta raga that highlights clarity and intensity, with its structure offering a meditative depth.",
  "cultural_significance": "This raga is used for both devotional and concert settings to highlight its intricate nature."
},
{
  "name": "Latangi",
  "arohana": "S R₂ G₃ M₂ P D₃ N₃ S",
  "avarohana": "S N₃ D₃ P M₂ G₃ R₂ S",
  "time_of_day": "Evening",
  "character": "Latangi is a raga of grace and beauty, evoking a sense of tenderness and subtle joy. Its melodic charm is soothing and deeply emotional.",
  "associated_deity_emotion": "Latangi is often associated with Lord Krishna, symbolizing love and compassion.",
  "popular_compositions": [
    "Marivere Dikkevarayya - Patnam Subramania Iyer",
    "Aparadhamula Norva - Tyagaraja"
  ],
  "history": "Latangi is one of the most popular melakarta ragas, known for its versatility and the emotional depth it conveys.",
  "cultural_significance": "It is widely used in concerts, particularly for emotional and expressive compositions."
},
{
  "name": "Vachaspati",
  "arohana": "S R₁ G₃ M₂ P D₂ N₃ S",
  "avarohana": "S N₃ D₂ P M₂ G₃ R₁ S",
  "time_of_day": "Morning",
  "character": "Vachaspati is a serene and meditative raga, known for its ability to evoke devotion and spiritual clarity.",
  "associated_deity_emotion": "Vachaspati is associated with Lord Brahma, symbolizing wisdom and creation.",
  "popular_compositions": [
    "Kanta Joodumi - Tyagaraja",
    "Paratpara Parameshwara - Muthuswami Dikshitar"
  ],
  "history": "Vachaspati has been a significant part of Carnatic tradition, favored for its rich and peaceful tonal quality.",
  "cultural_significance": "It is often performed in concerts as a reflective and deeply spiritual raga."
},
{
  "name": "Mechakalyani",
  "arohana": "S R₂ G₃ M₂ P D₂ N₃ S",
  "avarohana": "S N₃ D₂ P M₂ G₃ R₂ S",
  "time_of_day": "Evening",
  "character": "Mechakalyani is a majestic and bright raga, exuding positivity, grandeur, and elegance.",
  "associated_deity_emotion": "Mechakalyani is linked to Goddess Lakshmi, symbolizing wealth and auspiciousness.",
  "popular_compositions": [
    "Amba Kamakshi - Syama Sastri",
    "Nidhi Chala Sukhama - Tyagaraja"
  ],
  "history": "Mechakalyani is a cornerstone of Carnatic music, frequently explored by composers for its versatility and grandeur.",
  "cultural_significance": "It is often performed in both devotional and concert settings, showcasing its regal and uplifting nature."
},
{
  "name": "Chitrambari",
  "arohana": "S R₂ G₂ M₂ P D₂ N₃ S",
  "avarohana": "S N₃ D₂ P M₂ G₂ R₂ S",
  "time_of_day": "Afternoon",
  "character": "Chitrambari is a raga that evokes introspection and tranquility. It has a meditative quality with a slightly haunting undertone.",
  "associated_deity_emotion": "This raga is associated with Goddess Durga, reflecting protection and inner strength.",
  "popular_compositions": [
    "Sri Varalakshmi Namastubhyam - Muthuswami Dikshitar",
    "Tyagaraja Yoga Vaibhavam - Muthuswami Dikshitar"
  ],
  "history": "Chitrambari, though less frequently performed, holds a significant place in the melakarta scheme for its unique tonal structure.",
  "cultural_significance": "This raga is often employed in spiritual and devotional contexts, lending itself well to reflective compositions."
},
{
  "name": "Sucharitra",
  "arohana": "S R₁ G₃ M₂ P D₂ N₂ S",
  "avarohana": "S N₂ D₂ P M₂ G₃ R₁ S",
  "time_of_day": "Morning",
  "character": "Sucharitra is a peaceful raga that embodies simplicity and serenity. Its straightforward scale allows for deep emotional exploration.",
  "associated_deity_emotion": "Sucharitra is associated with Lord Vishnu, symbolizing purity and stability.",
  "popular_compositions": [
    "Sri Satyanarayanam - Muthuswami Dikshitar"
  ],
  "history": "Sucharitra is a rare melakarta raga that is often used for exploring gentle and serene themes.",
  "cultural_significance": "This raga's calmness makes it ideal for devotional and meditative pieces."
},
{
  "name": "Jyoti Swarupini",
  "arohana": "S R₃ G₃ M₂ P D₁ N₁ S",
  "avarohana": "S N₁ D₁ P M₂ G₃ R₃ S",
  "time_of_day": "Afternoon",
  "character": "Jyoti Swarupini is a raga with an unusual and unique structure that evokes mystery and spiritual fervor.",
  "associated_deity_emotion": "This raga is often linked to Lord Shiva, symbolizing cosmic energy and transformation.",
  "popular_compositions": [
    "Brihaspate Tarapathe - Muthuswami Dikshitar"
  ],
  "history": "Jyoti Swarupini is one of the lesser-known melakarta ragas, offering scope for creativity and emotional expression.",
  "cultural_significance": "This raga is appreciated for its innovative melodic possibilities in both devotional and concert settings."
},
{
  "name": "Dhatuvardani",
  "arohana": "S R₂ G₃ M₂ P D₃ N₂ S",
  "avarohana": "S N₂ D₃ P M₂ G₃ R₂ S",
  "time_of_day": "Evening",
  "character": "Dhatuvardani is a vibrant and lively raga, evoking feelings of joy and celebration.",
  "associated_deity_emotion": "Dhatuvardani is associated with Lord Krishna, symbolizing playful energy and charm.",
  "popular_compositions": [
    "Sri Saraswati Namostute - Koteeswara Iyer"
  ],
  "history": "Dhatuvardani, a lesser-known raga, is appreciated for its rich melodic patterns and lively character.",
  "cultural_significance": "This raga is often performed in festive and uplifting contexts, bringing a sense of dynamism to performances."
},
{
  "name": "Nasikabhushini",
  "arohana": "S R₃ G₃ M₂ P D₃ N₃ S",
  "avarohana": "S N₃ D₃ P M₂ G₃ R₃ S",
  "time_of_day": "Night",
  "character": "Nasikabhushini is a majestic raga with a bold and regal tone. It evokes a sense of grandeur and divinity.",
  "associated_deity_emotion": "This raga is linked to Lord Vishnu, representing protection and cosmic order.",
  "popular_compositions": [
    "Sri Rukmini Devi Sametha - Koteeswara Iyer"
  ],
  "history": "Nasikabhushini is a melakarta raga that has been used in devotional compositions, highlighting its grand character.",
  "cultural_significance": "The raga's commanding presence makes it a favorite for compositions focusing on devotion and praise."
},
{
  "name": "Kosalam",
  "arohana": "S R₁ G₃ M₂ P D₂ N₃ S",
  "avarohana": "S N₃ D₂ P M₂ G₃ R₁ S",
  "time_of_day": "Evening",
  "character": "Kosalam is a profound and meditative raga, known for its deep and solemn melodic contours.",
  "associated_deity_emotion": "Kosalam is often associated with Lord Rama, reflecting dharma and spiritual strength.",
  "popular_compositions": [
    "Kosala Natha - Muthuswami Dikshitar"
  ],
  "history": "Kosalam is a significant melakarta raga, known for its ability to evoke devotion and introspection.",
  "cultural_significance": "This raga is often performed in devotional contexts, focusing on introspective and philosophical themes."
},
{
  "name": "Rasikapriya",
  "arohana": "S R₃ G₃ M₂ P D₃ N₃ S",
  "avarohana": "S N₃ D₃ P M₂ G₃ R₃ S",
  "time_of_day": "Night",
  "character": "Rasikapriya is a majestic raga, filled with grandeur and sophistication. It exudes emotional depth and intensity.",
  "associated_deity_emotion": "This raga is associated with Lord Shiva, symbolizing cosmic power and transformation.",
  "popular_compositions": [
    "Ganapathe - Koteeswara Iyer",
    "Rasikapriya - GNB"
  ],
  "history": "Rasikapriya is the 72nd and final melakarta raga, showcasing the culmination of the melakarta system's structure.",
  "cultural_significance": "This raga is a staple in Carnatic music, representing the complexity and depth of the melakarta system."
},
{
  "name": "Suddha Dhanyasi",
  "arohana": "S G₂ M₁ P N₂ S",
  "avarohana": "S N₂ P M₁ G₂ S",
  "time_of_day": "Morning",
  "character": "Suddha Dhanyasi is a pentatonic raga that exudes simplicity, devotion, and tranquility. Its melody is soothing and often used in devotional compositions.",
  "associated_deity_emotion": "This raga is associated with Goddess Saraswati, symbolizing wisdom and purity.",
  "popular_compositions": [
    "Himagiri Tanaye - Muthiah Bhagavatar",
    "Subramanyena Rakshitoham - Muthuswami Dikshitar",
    "Enna Thavam Seithanai - Papanasam Sivan"
  ],
  "history": "Suddha Dhanyasi is a janya raga derived from the 22nd melakarta raga Kharaharapriya. Its simplicity and emotional appeal make it a favorite among listeners.",
  "cultural_significance": "It is widely performed in Carnatic music concerts, especially in devotional settings, for its meditative and uplifting quality."
},
{
  "name": "Revati",
  "arohana": "S R₁ M₁ P N₃ S",
  "avarohana": "S N₃ P M₁ R₁ S",
  "time_of_day": "Evening",
  "character": "Revati is a serene raga that evokes peace and meditation. It is often used in contemplative compositions.",
  "associated_deity_emotion": "This raga is associated with Lord Shiva, symbolizing calmness and transcendence.",
  "popular_compositions": [
    "Janani Mamava - Muthuswami Dikshitar",
    "Bho Shambho - Swami Dayananda Saraswati",
    "Paahi Parvatha Nandini - Muthiah Bhagavatar"
  ],
  "history": "Revati is an audava raga derived from Mayamalavagowla. Its simple structure and deep emotional resonance make it suitable for meditation and devotion.",
  "cultural_significance": "Revati is a popular choice for devotional and spiritual compositions in Carnatic music."
},
{
  "name": "Hamsadhwani",
  "arohana": "S R₂ G₃ P N₃ S",
  "avarohana": "S N₃ P G₃ R₂ S",
  "time_of_day": "Any time",
  "character": "Hamsadhwani is a bright and auspicious raga that conveys joy and positivity. It is often sung at the beginning of concerts.",
  "associated_deity_emotion": "This raga is dedicated to Lord Ganesha, symbolizing auspicious beginnings.",
  "popular_compositions": [
    "Vatapi Ganapatim - Muthuswami Dikshitar",
    "Raghunatha Nannu - Patnam Subramania Iyer",
    "Gajavadana Beduve - Purandaradasa"
  ],
  "history": "Hamsadhwani is a janya raga derived from the 29th melakarta, Dheerasankarabharanam. It is known for its uplifting and joyful appeal.",
  "cultural_significance": "This raga is a staple in Carnatic music and is performed widely across genres for its versatile and melodic nature."
},
{
  "name": "Mohanam",
  "arohana": "S R₂ G₃ P D₂ S",
  "avarohana": "S D₂ P G₃ R₂ S",
  "time_of_day": "Morning",
  "character": "Mohanam is a cheerful and light raga that evokes a sense of happiness and simplicity. It is universally appealing due to its pentatonic nature.",
  "associated_deity_emotion": "This raga is associated with Lord Krishna, symbolizing playfulness and love.",
  "popular_compositions": [
    "Nannu Palimpa - Tyagaraja",
    "Kapali - Papanasam Sivan",
    "Evarura Ninnuvina - Patnam Subramania Iyer"
  ],
  "history": "Mohanam is a pentatonic raga derived from the 28th melakarta, Harikambhoji. It is popular in both Carnatic and Hindustani music.",
  "cultural_significance": "Mohanam is frequently performed in concerts and is used in both classical and light music compositions."
},
{
  "name": "Kalyani",
  "arohana": "S R₂ G₃ M₂ P D₂ N₃ S",
  "avarohana": "S N₃ D₂ P M₂ G₃ R₂ S",
  "time_of_day": "Evening",
  "character": "Kalyani is a grand and versatile raga that conveys emotions ranging from devotion to romance. Its structure allows for extensive improvisation.",
  "associated_deity_emotion": "This raga is associated with Goddess Lakshmi, symbolizing prosperity and grace.",
  "popular_compositions": [
    "Amma Ravamma - Tyagaraja",
    "Vasudevayani - Tyagaraja",
    "Nijadasa Varada - Muthuswami Dikshitar"
  ],
  "history": "Kalyani is the 65th melakarta raga and is one of the most popular and extensively explored ragas in Carnatic music.",
  "cultural_significance": "It is a staple in Carnatic music, appearing in various forms such as varnams, kritis, and thillanas."
},
{
  "name": "Todi",
  "arohana": "S R₁ G₃ M₁ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Morning",
  "character": "Todi is a deeply emotional raga that conveys devotion, longing, and introspection. Its rich structure allows for intricate and profound musical exploration.",
  "associated_deity_emotion": "Todi is often associated with Lord Shiva, symbolizing surrender and devotion.",
  "popular_compositions": [
    "Kaddanuvariki - Tyagaraja",
    "Raju Vedala - Tyagaraja",
    "Gajavadana Sammodita - Muthuswami Dikshitar"
  ],
  "history": "Todi is one of the ancient and revered melakarta ragas in Carnatic music. It has been used extensively by composers for its emotional depth and spiritual resonance.",
  "cultural_significance": "Todi is frequently performed in classical concerts, often in elaborate renditions, for its rich melodic possibilities."
},
{
  "name": "Bhairavi",
  "arohana": "S R₂ G₂ M₁ P D₂ N₂ S",
  "avarohana": "S N₂ D₁ P M₁ G₂ R₂ S",
  "time_of_day": "Any time",
  "character": "Bhairavi is a majestic raga known for its grandeur and versatility, often used in both devotional and romantic contexts.",
  "associated_deity_emotion": "This raga is associated with Goddess Durga, symbolizing power and compassion.",
  "popular_compositions": [
    "Viriboni (Ata Tala Varnam) - Pachimiriyam Adiappayya",
    "Upacharamu - Tyagaraja",
    "Sri Kamalambikayam - Muthuswami Dikshitar"
  ],
  "history": "Bhairavi is a janya raga derived from the 20th melakarta Natabhairavi. Its adaptability makes it a favorite for both classical and semi-classical compositions.",
  "cultural_significance": "Bhairavi is widely performed in Carnatic concerts and is often featured in concluding pieces like thillanas or mangalam."
},
{
  "name": "Shankarabharanam",
  "arohana": "S R₂ G₃ M₁ P D₂ N₃ S",
  "avarohana": "S N₃ D₂ P M₁ G₃ R₂ S",
  "time_of_day": "Morning",
  "character": "Shankarabharanam is a majestic and versatile raga that conveys stability and grandeur. It is one of the fundamental ragas in Carnatic music.",
  "associated_deity_emotion": "This raga is associated with Lord Vishnu, symbolizing balance and harmony.",
  "popular_compositions": [
    "Enduku Peddala - Tyagaraja",
    "Sarabhanandana - Muthuswami Dikshitar",
    "Akshayalinga Vibho - Muthuswami Dikshitar"
  ],
  "history": "Shankarabharanam is the 29th melakarta raga and has been extensively explored in Carnatic and Hindustani music traditions.",
  "cultural_significance": "It is considered one of the most foundational ragas, often used in teaching and for large-scale improvisational pieces in concerts."
},
{
  "name": "Karaharapriya",
  "arohana": "S R₂ G₂ M₁ P D₂ N₂ S",
  "avarohana": "S N₂ D₂ P M₁ G₂ R₂ S",
  "time_of_day": "Evening",
  "character": "Karaharapriya is a soothing and deeply emotional raga that conveys compassion, love, and pathos.",
  "associated_deity_emotion": "This raga is often associated with Lord Rama, symbolizing his compassion and nobility.",
  "popular_compositions": [
    "Chakkaniraja - Tyagaraja",
    "Rama Nee Samanamevaru - Tyagaraja",
    "Pakkala Nilabadi - Tyagaraja"
  ],
  "history": "Karaharapriya is the 22nd melakarta raga and is known for its deeply evocative and melodic appeal.",
  "cultural_significance": "It is widely performed in Carnatic concerts and serves as the base for numerous janya ragas."
},
{
  "name": "Kambhoji",
  "arohana": "S R₂ G₃ M₁ P D₂ S",
  "avarohana": "S N₂ D₂ P M₁ G₃ R₂ S",
  "time_of_day": "Evening",
  "character": "Kambhoji is a majestic raga that conveys grandeur, love, and devotion. It is often used in elaborate compositions and improvisations.",
  "associated_deity_emotion": "This raga is associated with Lord Krishna, symbolizing his playful yet regal nature.",
  "popular_compositions": [
    "O Rangasayee - Tyagaraja",
    "Evari Mata - Tyagaraja",
    "Kailasanatha Gouri - Muthuswami Dikshitar"
  ],
  "history": "Kambhoji is a janya raga derived from the 28th melakarta Harikambhoji. Its grandeur and emotional depth make it a favorite among performers.",
  "cultural_significance": "Kambhoji is frequently performed in Carnatic concerts, often chosen for long and intricate renditions."
},
{
  "name": "Saveri",
  "arohana": "S R₁ M₁ P D₁ S",
  "avarohana": "S N₃ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Morning",
  "character": "Saveri is a meditative raga that conveys devotion, pathos, and a sense of humility. It is often used in compositions that emphasize introspection.",
  "associated_deity_emotion": "This raga is associated with Goddess Saraswati, symbolizing wisdom and devotion.",
  "popular_compositions": [
    "Rama Bana - Tyagaraja",
    "Darini Telusukonti - Syama Sastri",
    "Shankari Shankuru - Shyama Shastri"
  ],
  "history": "Saveri is a janya raga derived from the 15th melakarta Mayamalavagowla. Its structure and emotional appeal have made it popular in both classical and semi-classical forms.",
  "cultural_significance": "Saveri is frequently used in temple music and devotional performances, often emphasizing its soulful qualities."
},
{
  "name": "Kaanada",
  "arohana": "S G₃ M₁ P N₂ S",
  "avarohana": "S N₂ D₂ P M₁ G₃ R₂ S",
  "time_of_day": "Evening",
  "character": "Kaanada is a raga that conveys tenderness, love, and devotion. Its gentle, lilting phrases are deeply appealing to listeners.",
  "associated_deity_emotion": "This raga is often associated with Lord Krishna, symbolizing his playful and loving nature.",
  "popular_compositions": [
    "Emani Migula - Tyagaraja",
    "Amba Kamakshi - Syama Sastri",
    "Sukhi Evvaro - Tyagaraja"
  ],
  "history": "Kaanada is a janya raga derived from the 22nd melakarta Karaharapriya. It has a rich legacy in Carnatic music, known for its expressiveness.",
  "cultural_significance": "Kaanada is often used in both light and elaborate compositions, making it a favorite in concerts."
},
{
  "name": "Darbar",
  "arohana": "S R₂ M₁ P D₂ N₂ S",
  "avarohana": "S N₂ D₂ P M₁ G₃ R₂ S",
  "time_of_day": "Evening",
  "character": "Darbar is a regal raga known for its grandeur and dignity. It is often used in compositions that emphasize majesty and devotion.",
  "associated_deity_emotion": "This raga is associated with Lord Vishnu, symbolizing balance and stability.",
  "popular_compositions": [
    "Minakshi Memudam - Muthuswami Dikshitar",
    "Yochana Kamala Lochana - Tyagaraja",
    "Mundu Venuka - Tyagaraja"
  ],
  "history": "Darbar is a janya raga derived from the 22nd melakarta Karaharapriya. Its structure allows for intricate improvisations, making it a favorite among performers.",
  "cultural_significance": "Darbar is often performed in Carnatic concerts, particularly for its melodic depth and emotional resonance."
},
{
  "name": "Bilahari",
  "arohana": "S R₂ G₃ P D₂ S",
  "avarohana": "S N₂ D₂ P M₁ G₃ R₂ S",
  "time_of_day": "Morning",
  "character": "Bilahari is a cheerful and uplifting raga that conveys joy and celebration. It is often used in compositions that emphasize positivity.",
  "associated_deity_emotion": "This raga is associated with Lord Muruga, symbolizing youthful energy and exuberance.",
  "popular_compositions": [
    "Dorakuna Ituvanti Seva - Tyagaraja",
    "Paridana Michite - Patnam Subramania Iyer",
    "Sri Chamundeshwari - Mysore Vasudevacharya"
  ],
  "history": "Bilahari is a janya raga derived from the 29th melakarta Shankarabharanam. Its bright and energetic nature has made it a popular choice for both classical and light compositions.",
  "cultural_significance": "Bilahari is widely performed in concerts, often chosen for its lively and vibrant qualities."
},
{
  "name": "Begada",
  "arohana": "S G₃ R₂ G₃ M₁ P D₂ N₂ S",
  "avarohana": "S N₂ D₂ P M₁ G₃ R₂ S",
  "time_of_day": "Morning",
  "character": "Begada is a raga known for its elegance and charm. It conveys a sense of refined joy and devotion.",
  "associated_deity_emotion": "This raga is associated with Lord Vishnu, symbolizing grace and majesty.",
  "popular_compositions": [
    "Lalithe Sri - Muthuswami Dikshitar",
    "Thyagaraja Yoga Vaibhavam - Muthuswami Dikshitar",
    "Kamakshi - Syama Sastri"
  ],
  "history": "Begada is a janya raga derived from the 29th melakarta Shankarabharanam. Its unique phrasing and melodic beauty make it a classic in Carnatic music.",
  "cultural_significance": "Begada is frequently performed in concerts, often chosen for its melodic charm and versatility."
},
{
  "name": "Poorvikalyani",
  "arohana": "S R₂ G₃ M₂ P D₂ N₃ S",
  "avarohana": "S N₃ D₂ P M₂ G₃ R₂ S",
  "time_of_day": "Evening",
  "character": "Poorvikalyani is a raga that conveys devotion and serenity with a sense of deep emotion and longing. It is often chosen for its meditative quality.",
  "associated_deity_emotion": "This raga is often associated with Goddess Lakshmi, symbolizing grace and prosperity.",
  "popular_compositions": [
    "Meenakshi Memudam - Muthuswami Dikshitar",
    "Parama Pavana Rama - Tyagaraja",
    "Gnanamosagarada - Tyagaraja"
  ],
  "history": "Poorvikalyani is the 53rd melakarta in the Carnatic music system. It is highly regarded for its versatility in conveying both devotion and pathos.",
  "cultural_significance": "Poorvikalyani is frequently performed in concerts and is a favorite for both kritis and RTP (Ragam-Tanam-Pallavi) renditions."
},
{
  "name": "Madhyamavati",
  "arohana": "S R₂ M₁ P N₂ S",
  "avarohana": "S N₂ P M₁ R₂ S",
  "time_of_day": "Morning",
  "character": "Madhyamavati is a soothing and auspicious raga that conveys peace and serenity. It is often chosen for the conclusion of concerts.",
  "associated_deity_emotion": "This raga is associated with Lord Vishnu, symbolizing divinity and tranquility.",
  "popular_compositions": [
    "Vinayaka Ninnu Vina - Tyagaraja",
    "Dhyaname Varama - Tyagaraja",
    "Palaya Mam Parvata Nandini - Muthuswami Dikshitar"
  ],
  "history": "Madhyamavati is a pentatonic raga (audava raga) derived from the 22nd melakarta Karaharapriya. It is often performed at the end of concerts to signify closure and auspiciousness.",
  "cultural_significance": "Madhyamavati is considered highly auspicious and is commonly performed in both temple and concert settings."
},
{
  "name": "Yamunakalyani",
  "arohana": "S R₂ G₃ P M₂ P D₂ N₃ S",
  "avarohana": "S N₃ D₂ P M₂ G₃ R₂ S",
  "time_of_day": "Evening",
  "character": "Yamunakalyani is a raga known for its sweet and soothing quality. It conveys emotions of devotion, love, and longing.",
  "associated_deity_emotion": "This raga is associated with Lord Krishna, symbolizing love and divine connection.",
  "popular_compositions": [
    "Krishna Nee Begane - Vyasatirtha",
    "Haridasulu Vedalide - Annamacharya",
    "Jambupate Mam Pahi - Muthuswami Dikshitar"
  ],
  "history": "Yamunakalyani is a janya raga derived from the 65th melakarta Mechakalyani. Its emotive quality makes it a popular choice for devotional and light classical compositions.",
  "cultural_significance": "Yamunakalyani is widely performed in both classical and semi-classical concerts, often evoking a sense of divine love and serenity."
},
{
  "name": "Abhogi",
  "arohana": "S R₂ G₂ M₁ D₂ S",
  "avarohana": "S D₂ M₁ G₂ R₂ S",
  "time_of_day": "Morning",
  "character": "Abhogi is a raga known for its simplicity and depth. It conveys emotions of serenity and introspection.",
  "associated_deity_emotion": "This raga is often associated with Goddess Saraswati, symbolizing wisdom and creativity.",
  "popular_compositions": [
    "Sabapathikku Veru Daivam - Gopalakrishna Bharati",
    "Sri Lakshmi Varaham - Muthuswami Dikshitar",
    "Manasa Guruguha - Muthuswami Dikshitar"
  ],
  "history": "Abhogi is a pentatonic raga (audava raga) derived from the 22nd melakarta Karaharapriya. Its concise structure makes it a favorite for alapana and kritis.",
  "cultural_significance": "Abhogi is frequently performed in concerts and is a popular choice for light classical and devotional renditions."
},
{
  "name": "Shree",
  "arohana": "S R₂ M₁ P N₃ S",
  "avarohana": "S N₃ P M₁ G₃ R₂ S",
  "time_of_day": "Morning",
  "character": "Shree is a raga that conveys majesty and devotion. It is considered auspicious and meditative.",
  "associated_deity_emotion": "This raga is associated with Lord Vishnu, symbolizing his divine and regal qualities.",
  "popular_compositions": [
    "Endaro Mahanubhavulu - Tyagaraja",
    "Shree Varalakshmi Namastubhyam - Muthuswami Dikshitar",
    "Pahimam Shri Rajarajeshwari - Swathi Thirunal"
  ],
  "history": "Shree is a janya raga derived from the 22nd melakarta Karaharapriya. It has been used in both classical and semi-classical compositions for centuries.",
  "cultural_significance": "Shree is often performed in temple settings and concerts, particularly for its auspicious nature."
},
{
  "name": "Arabhi",
  "arohana": "S R₂ M₁ P D₂ S",
  "avarohana": "S N₃ D₂ P M₁ G₃ R₂ S",
  "time_of_day": "Morning",
  "character": "Arabhi is a raga that conveys energy, joy, and enthusiasm. Its bright and lively nature makes it a popular choice for compositions that express victory and praise.",
  "associated_deity_emotion": "Arabhi is often associated with Lord Ganesha, symbolizing strength and divine grace.",
  "popular_compositions": [
    "Sadhinchane O Manasa - Tyagaraja",
    "Sri Saraswati Namostute - Muthuswami Dikshitar",
    "Narayana Divyanama - Purandaradasa"
  ],
  "history": "Arabhi is a janya raga of the 29th melakarta Shankarabharanam. It has been widely used in both devotional and classical compositions.",
  "cultural_significance": "Arabhi is often performed in concerts and temple settings for its auspicious and uplifting nature."
},
{
  "name": "Anandabhairavi",
  "arohana": "S G₂ R₂ G₂ M₁ P D₂ P S",
  "avarohana": "S N₃ D₂ P M₁ G₂ R₂ S",
  "time_of_day": "Evening",
  "character": "Anandabhairavi is a raga that conveys tenderness and compassion. It is known for its deeply emotional and soothing quality.",
  "associated_deity_emotion": "This raga is often associated with Goddess Parvati, symbolizing maternal love and divine compassion.",
  "popular_compositions": [
    "O Jagadamba - Syama Sastri",
    "Marivere Gati - Patnam Subramania Iyer",
    "Kamalamba Samrakshatumam - Muthuswami Dikshitar"
  ],
  "history": "Anandabhairavi is a highly expressive raga with both Carnatic and Hindustani adaptations. It is traditionally associated with love and devotion.",
  "cultural_significance": "Anandabhairavi is frequently performed in concerts for its emotive quality and versatility in both kritis and padams."
},
{
  "name": "Nattai",
  "arohana": "S R₃ G₃ M₁ P N₃ S",
  "avarohana": "S N₃ P M₁ G₃ R₃ S",
  "time_of_day": "Morning",
  "character": "Nattai is a majestic and energetic raga, often chosen for invocatory pieces. It conveys power, vigor, and auspiciousness.",
  "associated_deity_emotion": "This raga is associated with Lord Ganesha, symbolizing divine energy and wisdom.",
  "popular_compositions": [
    "Jagadanandakaraka - Tyagaraja",
    "Swaminatha Paripalaya - Muthuswami Dikshitar",
    "Maha Ganapathim - Muthuswami Dikshitar"
  ],
  "history": "Nattai is a janya raga derived from the 36th melakarta Chalanata. It has been widely used in opening pieces of concerts for its auspicious and uplifting nature.",
  "cultural_significance": "Nattai is highly popular in concert performances and is often associated with invocatory prayers and rituals."
},
{
  "name": "Varali",
  "arohana": "S G₃ M₁ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Evening",
  "character": "Varali is a deeply emotional and meditative raga that conveys longing and surrender. Its unique structure makes it one of the most intricate ragas in Carnatic music.",
  "associated_deity_emotion": "Varali is associated with Lord Shiva, symbolizing deep devotion and spiritual awakening.",
  "popular_compositions": [
    "Ka Va Va - Papanasam Sivan",
    "Mamava Meenakshi - Muthuswami Dikshitar",
    "Eti Janmamidi - Tyagaraja"
  ],
  "history": "Varali is the 39th melakarta raga and has a distinct melodic structure. Its complex nature requires great skill to perform.",
  "cultural_significance": "Varali is commonly performed in classical concerts and is regarded as one of the most challenging and expressive ragas."
},
{
  "name": "Sahana",
  "arohana": "S R₂ G₃ M₁ P M₁ D₂ N₂ S",
  "avarohana": "S N₂ D₂ P M₁ G₃ R₂ S",
  "time_of_day": "Evening",
  "character": "Sahana is a raga that conveys tenderness, pathos, and compassion. Its emotive quality makes it a favorite for romantic and devotional compositions.",
  "associated_deity_emotion": "This raga is associated with Lord Vishnu, symbolizing divine love and compassion.",
  "popular_compositions": [
    "Giripai Nelakonna - Tyagaraja",
    "Vandanamu Raghunandana - Tyagaraja",
    "Rama Ika Nannu Brova - Tyagaraja"
  ],
  "history": "Sahana is a janya raga derived from the 28th melakarta Harikambhoji. Its lyrical beauty and emotive depth have made it a staple in Carnatic music.",
  "cultural_significance": "Sahana is frequently performed in concerts for its emotive quality and lyrical grace."
},
{
  "name": "Amritavarshini",
  "arohana": "S G₃ M₂ P N₃ S",
  "avarohana": "S N₃ P M₂ G₃ S",
  "time_of_day": "Any time of the day",
  "character": "Amritavarshini is a joyful and uplifting raga. It is believed to have the ability to invoke rain and is often associated with bringing positivity and auspiciousness.",
  "associated_deity_emotion": "Amritavarshini is often linked to Goddess Saraswati, symbolizing purity, learning, and creativity.",
  "popular_compositions": [
    "Anandamrita Karshini - Muthuswami Dikshitar",
    "Sudhamayi Sudhanidhi - Harikesanallur Muthiah Bhagavatar",
    "Pannagendra Shayana - Muthuswami Dikshitar"
  ],
  "history": "Amritavarshini is a derived raga and is unique for its pentatonic scale. Its cheerful and evocative sound has made it popular across centuries.",
  "cultural_significance": "The raga is known for its supposed connection to invoking rain and is performed during times of celebration and auspicious beginnings."
},
{
  "name": "Hindolam",
  "arohana": "S G₂ M₁ D₂ N₂ S",
  "avarohana": "S N₂ D₂ M₁ G₂ S",
  "time_of_day": "Evening",
  "character": "Hindolam is a meditative and calming raga. It is often used to evoke feelings of devotion, tranquility, and introspection.",
  "associated_deity_emotion": "Hindolam is often associated with Lord Krishna, symbolizing joy and spiritual bliss.",
  "popular_compositions": [
    "Samaja Vara Gamana - Tyagaraja",
    "Niravadhi Sukhada - Tyagaraja",
    "Mamava Meenakshi - Muthuswami Dikshitar"
  ],
  "history": "Hindolam is a pentatonic scale and has parallels in Hindustani music as Malkauns. It is highly versatile and has been adapted in both classical and semi-classical genres.",
  "cultural_significance": "Hindolam is popular in concerts for its soothing effect and is often used in thematic presentations focused on devotion and spirituality."
},
{
  "name": "Pantuvarali",
  "arohana": "S R₁ G₃ M₂ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₂ G₃ R₁ S",
  "time_of_day": "Morning",
  "character": "Pantuvarali conveys intensity, pathos, and longing. It is a raga that evokes deep spiritual yearning and is suited for emotionally charged compositions.",
  "associated_deity_emotion": "Pantuvarali is often associated with Lord Shiva, symbolizing surrender and devotion.",
  "popular_compositions": [
    "Sarasaksha Paripalaya - Swathi Thirunal",
    "Shiva Shiva Ena Radha - Tyagaraja",
    "Ennalu Urake - Tyagaraja"
  ],
  "history": "Pantuvarali is the 51st melakarta raga in Carnatic music. Its intense emotional depth has made it a favorite for devotional and classical performances.",
  "cultural_significance": "The raga is frequently performed in concerts and is considered a powerful medium for expressing deep spiritual emotions."
},
{
  "name": "Janaranjani",
  "arohana": "S R₂ G₃ M₁ P D₂ N₃ S",
  "avarohana": "S N₃ D₂ P M₁ G₃ R₂ S",
  "time_of_day": "Evening",
  "character": "Janaranjani is a melodious raga known for its gentle and pleasant nature. It is often used for compositions that are light and pleasing to the listener.",
  "associated_deity_emotion": "This raga is associated with Lord Vishnu, symbolizing peace and grace.",
  "popular_compositions": [
    "Vidajaladura - Tyagaraja",
    "Paripahimam - Papanasam Sivan",
    "Nee Pamaela Naama - Harikesanallur Muthiah Bhagavatar"
  ],
  "history": "Janaranjani is a janya raga derived from the 29th melakarta Shankarabharanam. Its simplicity and elegance have made it popular for lighter classical pieces.",
  "cultural_significance": "The raga is often performed in concerts as a lighter interlude, providing a soothing break in the concert repertoire."
},
{
  "name": "Yamunakalyani",
  "arohana": "S R₂ G₃ M₁ P D₂ N₃ S",
  "avarohana": "S N₃ D₂ P M₁ G₃ R₂ S",
  "time_of_day": "Evening",
  "character": "Yamunakalyani is a raga that conveys sweetness, devotion, and tranquility. It is often used for compositions that celebrate divine love and grace.",
  "associated_deity_emotion": "This raga is associated with Lord Krishna and Radha, symbolizing divine love and beauty.",
  "popular_compositions": [
    "Krishna Nee Begane Baro - Vyasaraya Tirtha",
    "Bhavayami Gopalabalam - Annamacharya",
    "Jambupate - Muthuswami Dikshitar"
  ],
  "history": "Yamunakalyani is a janya raga derived from the 65th melakarta Kalyani. Its lyrical beauty has made it a favorite for bhajans and lighter classical compositions.",
  "cultural_significance": "The raga is extensively performed in concerts and devotional settings, often chosen for its melodious and graceful appeal."
},
{
  "name": "Manirangu",
  "arohana": "S R₁ G₃ M₁ P D₁ N₂ S",
  "avarohana": "S N₂ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Evening",
  "character": "Manirangu is a lively and energetic raga that brings a sense of exuberance and joy. It conveys feelings of playfulness, celebration, and vitality.",
  "associated_deity_emotion": "Manirangu is often associated with Lord Vishnu and Lord Krishna, evoking feelings of divine playfulness, joy, and devotion.",
  "popular_compositions": [
    "Rama Ni Nama - Tyagaraja",
    "Manirangu Varnam - Various Composers",
    "Sarvamangala - Muthuswami Dikshitar"
  ],
  "history": "Manirangu is a janya raga derived from the 29th melakarta raga Shankarabharanam. It is known for its cheerful and uplifting mood and is popular in both classical and devotional music.",
  "cultural_significance": "Manirangu is often performed during festive occasions and in concerts where a lively atmosphere is desired."
},
{
  "name": "Vasantha",
  "arohana": "S R₁ G₃ M₁ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Morning",
  "character": "Vasantha is a serene and soothing raga that evokes feelings of peace, tranquility, and the beauty of nature. It brings about a sense of serenity and calmness.",
  "associated_deity_emotion": "Vasantha is associated with Lord Vishnu and Lord Rama, symbolizing peace, auspiciousness, and beauty in nature.",
  "popular_compositions": [
    "Vasantha Varnam - Various Composers",
    "Vasantha Svarajati - Muthuswami Dikshitar",
    "Bhavayami Gopalabalam - Tyagaraja"
  ],
  "history": "Vasantha is a raga that is known for its calm and meditative qualities. It is often performed at the beginning of concerts, providing a peaceful introduction.",
  "cultural_significance": "Vasantha is frequently performed during auspicious occasions and festivals, evoking the beauty of spring and nature."
},
{
  "name": "Surutti",
  "arohana": "S R₁ G₃ M₁ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Late Evening",
  "character": "Surutti is a raga known for its gentle, sweet, and soothing character. It conveys feelings of peace, affection, and sweetness, often used to calm the mind and heart.",
  "associated_deity_emotion": "Surutti is associated with Lord Shiva, symbolizing tranquility, devotion, and spiritual bliss.",
  "popular_compositions": [
    "Rama Ni Nama - Tyagaraja",
    "Sitarama Kalyana - Muthuswami Dikshitar",
    "Tungabhadra - Tyagaraja"
  ],
  "history": "Surutti is a raga that has been praised for its emotional depth and versatility. It is a highly respected raga in Carnatic music for its melodic sweetness and calming effect.",
  "cultural_significance": "Surutti is frequently performed in devotional contexts and often used in concerts to create a tranquil atmosphere."
},
{
  "name": "Desh",
  "arohana": "S R₁ G₃ M₁ P D₁ N₂ S",
  "avarohana": "S N₂ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Monsoon",
  "character": "Desh is a raga that evokes feelings of devotion, joy, and a sense of celebration. It is characterized by a joyful, uplifting, and energetic mood.",
  "associated_deity_emotion": "Desh is associated with Lord Vishnu and Lord Krishna, evoking feelings of divine grace, devotion, and bliss.",
  "popular_compositions": [
    "Madhurastakam - Adi Shankaracharya",
    "Chandram Bhaja - Muthuswami Dikshitar",
    "Raghupati Raghava - Ramdas"
  ],
  "history": "Desh is a popular raga in both Hindustani and Carnatic music traditions. In Carnatic music, it is known for its festive and celebratory mood, often performed during monsoon-related themes.",
  "cultural_significance": "Desh is frequently performed during festive occasions and is known to evoke feelings of joy and happiness in listeners."
},
{
  "name": "Harikambhoji",
  "arohana": "S R₁ G₃ M₁ P D₁ N₂ S",
  "avarohana": "S N₂ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Morning",
  "character": "Harikambhoji is a majestic and devotional raga that conveys a deep sense of reverence, devotion, and peace. It is often used to express divine love and yearning.",
  "associated_deity_emotion": "Harikambhoji is associated with Lord Vishnu, symbolizing divine grace, reverence, and spiritual bliss.",
  "popular_compositions": [
    "Venkatesa Suprabhatam - Various Composers",
    "Eka Dantam - Muthuswami Dikshitar",
    "Narayana Sankeerthanam - Tyagaraja"
  ],
  "history": "Harikambhoji is a revered raga in Carnatic music and has been a favorite in devotional music due to its majestic and spiritual qualities. It is also one of the 72 melakarta ragas.",
  "cultural_significance": "Harikambhoji is frequently performed in religious settings, particularly during early morning concerts and rituals, where it helps evoke a sense of devotion and peace."
},
{
  "name": "Mukhari",
  "arohana": "S R₁ G₃ M₁ P D₁ N₂ S",
  "avarohana": "S N₂ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Morning",
  "character": "Mukhari is a raga that conveys a feeling of emotional depth and solemnity. It evokes a sense of tranquility, introspection, and devotion.",
  "associated_deity_emotion": "Mukhari is associated with Lord Shiva, symbolizing peace, surrender, and devotion.",
  "popular_compositions": [
    "Jagadananda Karaka - Tyagaraja",
    "Mukhari Varnam - Various Composers",
    "Samastha Lokah - Tyagaraja"
  ],
  "history": "Mukhari is a raga that has been cherished for centuries for its devotional and emotional qualities. It is a melakarta raga and is often used in compositions that explore themes of devotion.",
  "cultural_significance": "Mukhari is frequently performed during spiritual and devotional concerts, and its slow tempo allows for deep emotional expression."
},
{
  "name": "Ranjani",
  "arohana": "S R₁ G₃ M₁ P D₂ N₃ S",
  "avarohana": "S N₃ D₂ P M₁ G₃ R₁ S",
  "time_of_day": "Night",
  "character": "Ranjani is a raga that conveys feelings of joy, playfulness, and exuberance. It is often used to create an uplifting and energetic mood.",
  "associated_deity_emotion": "Ranjani is associated with Goddess Saraswati, symbolizing creativity, knowledge, and auspiciousness.",
  "popular_compositions": [
    "Narayana Gajendra - Tyagaraja",
    "Ranjani Varnam - Various Composers",
    "Kamakshi Amba - Muthuswami Dikshitar"
  ],
  "history": "Ranjani is known for its uplifting and joyful qualities and has been a favorite for performances that aim to energize and uplift listeners. It is also derived from the 29th melakarta raga Shankarabharanam.",
  "cultural_significance": "Ranjani is commonly performed in celebratory or devotional settings and is cherished for its lively, auspicious mood."
},
{
  "name": "Kapi",
  "arohana": "S R₁ G₃ M₁ P D₁ N₃ S",
  "avarohana": "S N₃ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Night",
  "character": "Kapi is a raga that conveys a deep sense of longing, devotion, and melancholy. It has an emotional weight that evokes feelings of yearning, often associated with a sense of separation from the divine or a loved one.",
  "associated_deity_emotion": "Kapi is often associated with Lord Rama, expressing devotion, longing, and separation. It is believed to bring out feelings of heartfelt devotion and attachment.",
  "popular_compositions": [
    "Rama Nannu Brovara - Tyagaraja",
    "Enna Tavam - Muthuswami Dikshitar",
    "Raghupathi Raghava - Ramdas"
  ],
  "history": "Kapi is a classical raga with roots in both Hindustani and Carnatic music traditions. It is a popular raga that is often used in compositions expressing intense devotion and emotional depth.",
  "cultural_significance": "Kapi is frequently performed in devotional and emotional compositions, often highlighting themes of separation and yearning. It is a beloved raga in Carnatic music, widely appreciated for its emotional resonance."
},
{
  "name": "Simhavahini",
  "arohana": "S R₁ G₃ M₁ P D₁ N₂ S",
  "avarohana": "S N₂ D₁ P M₁ G₃ R₁ S",
  "time_of_day": "Morning",
  "character": "Simhavahini is a powerful and majestic raga that conveys courage, valor, and strength. It is often associated with the might and grace of a lion, evoking feelings of heroism, confidence, and majesty.",
  "associated_deity_emotion": "Simhavahini is associated with Goddess Durga, symbolizing strength, power, and protection. The raga expresses the divine energy of the goddess in her fierce form.",
  "popular_compositions": [
    "Simhavahini Varnam - Various Composers",
    "Mahishasura Mardini Stotra - Muthuswami Dikshitar",
    "Durga Ashtakshara Stotra - Tyagaraja"
  ],
  "history": "Simhavahini is a rare and powerful raga that is noted for its association with Goddess Durga and her warrior form. It has a regal and imposing sound, making it suitable for compositions that reflect valor and triumph.",
  "cultural_significance": "Simhavahini is often performed in the context of devotion to Goddess Durga, particularly during festivals such as Navaratri, where its strength and majesty complement the celebration of the goddess’s power."
}
]
