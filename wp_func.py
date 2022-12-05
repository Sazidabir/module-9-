def wp_p(p_text):
    code = f"<!-- wp:paragraph --><p>{p_text}</p><!-- /wp:paragraph -->"
    return code


def wp_h2(heading_text):
    code = f"<!-- wp:heading --><h2>{heading_text}</h2><!-- /wp:heading -->"
    return code

# demo = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."
#
# p = wp_paragraph(demo)
# print(p)