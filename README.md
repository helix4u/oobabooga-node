## Oobabooga

This is a node for InvokeAI 3.x, which calls a local instance of Oobabooga's Text-Generation-Webui and asks for a complex prompt based on the user's input.

### Example :

"describe a new mystical  creature in its natural environment"

*can return*

"The mystical creature I am describing to you is called the "Glimmerwing". It is a majestic, iridescent being that inhabits the depths of the most enchanted forests and glimmering lakes. Its body is covered in shimmering scales that reflect every color of the rainbow, and it has delicate, translucent wings that sparkle like diamonds in the sunlight. The Glimmerwing's home is a crystal-clear lake, surrounded by towering trees with leaves that shimmer like jewels. In this serene environment, the Glimmerwing spends its days swimming gracefully through the water, chasing schools of glittering fish and playing with the gentle ripples of the lake's surface.
As the sun sets, the Glimmerwing perches on a branch of one of the trees, spreading its wings to catch the last rays of light. The creature's scales glow softly, casting a rainbow of colors across the forest floor. The Glimmerwing sings a haunting melody, its voice echoing through the stillness of the night air. Its song is said to have the power to heal the sick and bring peace to troubled souls. Those who are lucky enough to hear the Glimmerwing's song are forever changed by its beauty and grace."

![glimmerwing_small](https://github.com/sammyf/oobabooga-node/assets/42468608/cecdd820-93dd-4c35-abbf-607e001fb2ed)

### Requirement :

a Text-Generation-Webui instance (might work remotely too, but I never tried it) and obviously InvokeAI 3.x

### Note :

this node works best with SDXL models, especially as the style can be described independantly of the LLM's output.
