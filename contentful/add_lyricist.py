from contentful.utils import create_entry

lyricist_data = [
    #{"lyricistName": "Vairamuthu", "lyricistId": "vairamuthu", "wikipediaUrl": ""},
    {"lyricistName": "Rajashri", "lyricistId": "rajashri", "wikipediaUrl": "https://en.wikipedia.org/wiki/Rajasri_(writer)"},
    #{"lyricistName": "Bichu Thirumala", "lyricistId": "bichu_thirumala", "wikipediaUrl": ""},
    #{"lyricistName": "Vaali", "lyricistId": "vaali", "wikipediaUrl": ""},
    {"lyricistName": "Kadhir", "lyricistId": "kadhir", "wikipediaUrl": "https://en.wikipedia.org/wiki/Kathir"},
    {"lyricistName": "Malgudi Subha", "lyricistId": "malgudi_subha", "wikipediaUrl": "https://en.wikipedia.org/wiki/Malgudi_Subha"},
    {"lyricistName": "PK Mishra", "lyricistId": "pk_mishra", "wikipediaUrl": "https://en.wikipedia.org/wiki/P._K._Mishra"},
    {"lyricistName": "Mankombu Gopalakrishnan", "lyricistId": "mankombu_gopalakrishnan", "wikipediaUrl": "https://en.wikipedia.org/wiki/Mankombu_Gopalakrishnan"},
    {"lyricistName": "NA Kamarasan", "lyricistId": "na_kamarasan", "wikipediaUrl": "https://en.wikipedia.org/wiki/Na._Kamarasan"},
    {"lyricistName": "Vennelekanti", "lyricistId": "vennelekanti", "wikipediaUrl": "https://en.wikipedia.org/wiki/Vennelakanti_(writer)"},
    {"lyricistName": "Noell James", "lyricistId": "noell_james", "wikipediaUrl": "https://www.imdb.com/name/nm1147220/"},
    #{"lyricistName": "Veturi Sundararama Murthy", "lyricistId": "veturi_sundararama_murthy", "wikipediaUrl": "https://en.wikipedia.org/wiki/Veturi"},
    {"lyricistName": "Sahiti", "lyricistId": "sahiti", "wikipediaUrl": ""},
    {"lyricistName": "Mehboob", "lyricistId": "mehboob", "wikipediaUrl": "https://en.wikipedia.org/wiki/Mehboob_Kotwal"},
    {"lyricistName": "Sivaganesh", "lyricistId": "sivaganesh", "wikipediaUrl": ""},
    {"lyricistName": "D Narayanavarma", "lyricistId": "d_narayanavarma", "wikipediaUrl": "https://www.imdb.com/name/nm9770623/"},
    {"lyricistName": "Jaladi Raja Rao", "lyricistId": "jaladi_raja_rao", "wikipediaUrl": "https://en.wikipedia.org/wiki/Jaladi_Raja_Rao"},
    #{"lyricistName": "Sirivennela Sitarama Sastry", "lyricistId": "sirivennela_sitarama_sastry_", "wikipediaUrl": "https://en.wikipedia.org/wiki/Sirivennela_Seetharama_Sastry"},
    {"lyricistName": "Bhuvana Chandra", "lyricistId": "bhuvana_chandra", "wikipediaUrl": "https://en.wikipedia.org/wiki/Bhuvana_Chandra"},
    {"lyricistName": "Ghantasala Ratnakumar", "lyricistId": "ghantasala_ratnakumar", "wikipediaUrl": ""},
    {"lyricistName": "Kambar", "lyricistId": "kambar", "wikipediaUrl": "https://en.wikipedia.org/wiki/Kambar_(poet)"},
    {"lyricistName": "S Shankar", "lyricistId": "s_shankar", "wikipediaUrl": "https://en.wikipedia.org/wiki/S._Shankar"},
    {"lyricistName": "Thirikudarasappa Kavirayar", "lyricistId": "thirikudarasappa_kavirayar", "wikipediaUrl": ""},
    {"lyricistName": "Pazhani Bharathi", "lyricistId": "pazhani_bharathi", "wikipediaUrl": "https://en.wikipedia.org/wiki/Palani_Bharathi"},
    {"lyricistName": "Guru Charan", "lyricistId": "guru_charan", "wikipediaUrl": "https://www.imdb.com/name/nm5738530/"},
    {"lyricistName": "Bharathi Babu", "lyricistId": "bharathi_babu", "wikipediaUrl": ""},
    {"lyricistName": "Kalidasan", "lyricistId": "kalidasan", "wikipediaUrl": ""},
    {"lyricistName": "Jagadish Khebudkar", "lyricistId": "jagadish_khebudkar", "wikipediaUrl": "https://en.wikipedia.org/wiki/Jagdish_Khebudkar"},
    {"lyricistName": "Irayimman Thampi", "lyricistId": "irayimman_thampi", "wikipediaUrl": "https://en.wikipedia.org/wiki/Irayimman_Thampi"},
    {"lyricistName": "Apache Indian", "lyricistId": "apache_indian", "wikipediaUrl": "https://en.wikipedia.org/wiki/Apache_Indian_(musician)"},
    {"lyricistName": "Bankim Chandra Chatterjee", "lyricistId": "bankim_chandra_chatterjee", "wikipediaUrl": "https://en.wikipedia.org/wiki/Bankim_Chandra_Chatterjee"},
    {"lyricistName": "Gulzar", "lyricistId": "gulzar", "wikipediaUrl": "https://en.wikipedia.org/wiki/Gulzar"},
    {"lyricistName": "Tim Kody", "lyricistId": "tim_kody", "wikipediaUrl": ""},
    {"lyricistName": "Dinesh Kapoor", "lyricistId": "dinesh_kapoor", "wikipediaUrl": ""},
    {"lyricistName": "Kanika Myer", "lyricistId": "kanika_myer", "wikipediaUrl": "https://www.imdb.com/name/nm0080241/"},
    {"lyricistName": "Sukhwinder Singh", "lyricistId": "sukhwinder_singh", "wikipediaUrl": "https://en.wikipedia.org/wiki/Sukhwinder_Singh"},
    {"lyricistName": "Javed Akhtar", "lyricistId": "javed_akhtar", "wikipediaUrl": "https://en.wikipedia.org/wiki/Javed_Akhtar"},
    {"lyricistName": "Gireesh Puthenchery", "lyricistId": "gireesh_puthenchery", "wikipediaUrl": "https://en.wikipedia.org/wiki/Girish_Puthenchery"},
    {"lyricistName": "Anand Bakshi", "lyricistId": "anand_bakshi", "wikipediaUrl": "https://en.wikipedia.org/wiki/Anand_Bakshi"},
    {"lyricistName": "Majrooh Sultanpuri", "lyricistId": "majrooh_sultanpuri", "wikipediaUrl": "https://en.wikipedia.org/wiki/Majrooh_Sultanpuri"},
    {"lyricistName": "Oothukkadu Venkatasubba Iyer", "lyricistId": "oothukkadu_venkatasubba_iyer", "wikipediaUrl": "https://en.wikipedia.org/wiki/Oothukkadu_Venkata_Kavi"},
    {"lyricistName": "Subramaniya Bharathi", "lyricistId": "subramaniya_bharathi", "wikipediaUrl": "https://en.wikipedia.org/wiki/Subramania_Bharati"},
    {"lyricistName": "Shaukat Ali", "lyricistId": "shaukat_ali", "wikipediaUrl": "https://en.wikipedia.org/wiki/Shaukat_Ali_(politician)"},
    {"lyricistName": "Thamarai", "lyricistId": "thamarai", "wikipediaUrl": "https://en.wikipedia.org/wiki/Thamarai"},
    {"lyricistName": "Pa Vijay", "lyricistId": "pa_vijay", "wikipediaUrl": "https://en.wikipedia.org/wiki/Pa._Vijay"},
    {"lyricistName": "Ilayakamban", "lyricistId": "ilayakamban", "wikipediaUrl": "https://www.imdb.com/name/nm5833169/"},
    {"lyricistName": "Arivumathi", "lyricistId": "arivumathi", "wikipediaUrl": "https://en.wikipedia.org/wiki/Arivumathi"},
    {"lyricistName": "Piraisoodan", "lyricistId": "piraisoodan", "wikipediaUrl": "https://en.wikipedia.org/wiki/Piraisoodan"},
    {"lyricistName": "Kalaikumar", "lyricistId": "kalaikumar", "wikipediaUrl": "https://www.imdb.com/name/nm7327850/"},
    {"lyricistName": "Samavedam Shanmukha Sarma", "lyricistId": "samavedam_shanmukha_sarma", "wikipediaUrl": "https://en.wikipedia.org/wiki/Samavedam_Shanmukha_Sarma"},
    {"lyricistName": "Na Muthukumar", "lyricistId": "na_muthukumar", "wikipediaUrl": "https://en.wikipedia.org/wiki/Na._Muthukumar"},
    {"lyricistName": "Rabindranath Tagore", "lyricistId": "rabindranath_tagore", "wikipediaUrl": "https://en.wikipedia.org/wiki/Rabindranath_Tagore"},
    {"lyricistName": "BH Abdul Hameed", "lyricistId": "bh_abdul_hameed", "wikipediaUrl": "https://en.wikipedia.org/wiki/B._H._Abdul_Hameed"},
    {"lyricistName": "Sameer Anjaan", "lyricistId": "sameer_anjaan", "wikipediaUrl": "https://en.wikipedia.org/wiki/Sameer_Anjaan"},
    {"lyricistName": "Blaaze", "lyricistId": "blaaze", "wikipediaUrl": "https://en.wikipedia.org/wiki/Blaaze"}
]
def create_lyricist_payload():
    """
    Create a payload for adding a new lyricist to Contentful.
    
    :return: A dictionary representing the lyricist entry payload.
    """
    for lyricist in lyricist_data:
        lyricist_id = lyricist.get('lyricistId', '').lower()
        lyricist_name = lyricist.get('lyricistName', '')
        wikipedia_url = lyricist.get('wikipediaUrl', '')

        entry_attributes = {
            'content_type_id': 'lyricist',
            'fields': { 
                'lyricistId': {
                    'en-US':lyricist_id
                },
                'lyricistName': {
                    'en-US': lyricist_name
                },
                'wikipediaUrl': {
                    'en-US': wikipedia_url
                }
            }
        }

        lyricist_entry = create_entry(lyricist_id, entry_attributes)
        print(f"Created entry for {lyricist_name} with ID: {lyricist_id}")