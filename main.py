import pywrapfst as fst

def create_am_latin_transducer(am_doc):
    amharic_latin_fst = fst.Fst()

    start_state = amharic_latin_fst.add_state()
    final_state = amharic_latin_fst.add_state()
    amharic_latin_fst.set_start(start_state)
    amharic_latin_fst.set_final(final_state)


    for amharic, latin in am_doc.items():
        amharic_state = amharic_latin_fst.add_state()
        latin_state = amharic_latin_fst.add_state()

        amharic_latin_fst.add_arc(start_state, amharic_state, 0,0)
        amharic_latin_fst.add_arc(amharic_state, latin_state, amharic, latin)
        amharic_latin_fst.add_arc(latin_state, final_state, 0, 0)

    return amharic_latin_fst

def main():
    amharic_to_latin_mapping = {

            }



