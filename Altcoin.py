
import requests


def altcoin_handler(x1,x2=None):

    response = requests.get('https://api.altcointrader.co.za/v3/live-stats')
    full_response = response.text

    if x1 in full_response or x1 == "all":

        # Cleaning up the output...
        n = full_response.count(",")
        full_response0 = full_response.replace(",", "", n)
        n = full_response.count("\"")
        full_response1 = full_response0.replace("\"", "", n)
        n = full_response.count("{")
        full_response2 = full_response1.replace("{", "", n)
        n = full_response.count("}")

        full_response3 = full_response2.replace("}", "", n)
        # full_response3 is the final clean version of all the data.
        if x1 == "all":
            print(full_response3)
            return full_response3  # full_response3 is the final clean version of all the data.

        else:
            full_response4 = full_response2[full_response2.index(x1):len(full_response2)]
            start_point = 0
            end_point = full_response4.index("}")
            finale_response = full_response4[start_point:end_point]
            # The finale_response is all the data for one specific coin.

            if x2 is None:

                print(finale_response)  # The finale_response is all the data for one specific coin.
                return finale_response

            elif x2 is not None:

                if x2 in finale_response:

                    data_piece = finale_response[finale_response.index(x2):len(finale_response)]
                    data_start_point = 0
                    data_end_point = data_piece.index(".")
                    data_end_point = data_end_point +2
                    finale_data_piece = data_piece[data_start_point:data_end_point]

                    # The finale_data_piece is the specific piece of data of a specific coin.
                    print(x1 + ": " + finale_data_piece)
                    return x1 + ": " + finale_data_piece

                else:
                    print("Error: the second variable does not match any of the pre programed variables")
                    return "Error: the second variable does not match any of the pre programed variables"

    elif x1 not in full_response:
        print("Error: the first variable does not match any of the pre programed variables")
        return "Error: the first variable does not match any of the pre programed variables"


altcoin_handler("XRP", "High")

