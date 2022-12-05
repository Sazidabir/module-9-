import wp_func

first_paragraph_text = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."

# first_paragraph_code = f"<!-- wp:paragraph --><p>{first_paragraph_text}</p><!-- /wp:paragraph -->"

heading_one_text = "Why do we use it?"
# heading_one_code = f"<!-- wp:heading --><h2>{heading_one_text}</h2><!-- /wp:heading -->"

second_paragraph_text = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."


article = wp_func.wp_p(first_paragraph_text)+wp_func.wp_h2(heading_one_text)+wp_func.wp_p(second_paragraph_text)

print(article)