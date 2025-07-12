from contentful.utils import create_entry

singer_data = [
    {"singerName": "Udit Narayan", "singerId": "udit_narayan", "wikipediaUrl": "https://en.wikipedia.org/wiki/Udit_Narayan"},
    {"singerName": "Biju Narayanan", "singerId": "biju_narayanan", "wikipediaUrl": "https://en.wikipedia.org/wiki/Biju_Narayanan"},
    {"singerName": "G Venugopal", "singerId": "g_venugopal", "wikipediaUrl": "https://en.wikipedia.org/wiki/G._Venugopal"},
    {"singerName": "Vani Jayaram", "singerId": "vani_jayaram", "wikipediaUrl": "https://en.wikipedia.org/wiki/Vani_Jairam"},
    {"singerName": "Noel James", "singerId": "noel_james", "wikipediaUrl": ""},
    {"singerName": "Prabhu Ganesan", "singerId": "prabhu_ganesan", "wikipediaUrl": "https://en.wikipedia.org/wiki/Prabhu_(actor)"},
    {"singerName": "Sreeja Ravi", "singerId": "sreeja_ravi", "wikipediaUrl": "https://en.wikipedia.org/wiki/Sreeja_Ravi"},
    {"singerName": "Vandemataram Srinivas", "singerId": "vandemataram_srinivas", "wikipediaUrl": "https://en.wikipedia.org/wiki/Vandemataram_Srinivas"},
    {"singerName": "Nabaron Ghosh", "singerId": "nabaron_ghosh", "wikipediaUrl": ""},
    {"singerName": "Alka Yagnik", "singerId": "alka_yagnik", "wikipediaUrl": "https://en.wikipedia.org/wiki/Alka_Yagnik"},
    {"singerName": "Shweta Shetty", "singerId": "shweta_shetty", "wikipediaUrl": "https://en.wikipedia.org/wiki/Shweta_Shetty"},
    {"singerName": "Asha Bhonsle", "singerId": "asha_bhonsle", "wikipediaUrl": "https://en.wikipedia.org/wiki/Asha_Bhosle"},
    {"singerName": "Kavita Krishnamurthy", "singerId": "kavita_krishnamurthy", "wikipediaUrl": "https://en.wikipedia.org/wiki/Kavita_Krishnamurthy"},
    {"singerName": "Shobha Shankar", "singerId": "shobha_shankar", "wikipediaUrl": ""},
    {"singerName": "Manorama", "singerId": "manorama", "wikipediaUrl": "https://en.wikipedia.org/wiki/Manorama_(Tamil_actress)"},
    {"singerName": "Suneeta Rao", "singerId": "suneeta_rao", "wikipediaUrl": "https://en.wikipedia.org/wiki/Suneeta_Rao"},
    {"singerName": "Unnikrishnan", "singerId": "unnikrishnan", "wikipediaUrl": "https://en.wikipedia.org/wiki/Unnikrishnan"},
    {"singerName": "Gopal Rao", "singerId": "gopal_rao", "wikipediaUrl": "https://www.imdb.com/name/nm1521934/"},
    {"singerName": "Theni Kunjaramma", "singerId": "theni_kunjaramma", "wikipediaUrl": "https://en.wikipedia.org/wiki/Theni_Kunjarammal"},
    {"singerName": "SPB Pallavi", "singerId": "spb_pallavi", "wikipediaUrl": ""},
    {"singerName": "Shankar Mahadevan", "singerId": "shankar_mahadevan", "wikipediaUrl": "https://en.wikipedia.org/wiki/Shankar_Mahadevan"},
    {"singerName": "Bharathi Raja", "singerId": "bharathi_raja", "wikipediaUrl": "https://en.wikipedia.org/wiki/Bharathiraja"},
    {"singerName": "Rajagopal", "singerId": "rajagopal", "wikipediaUrl": ""},
    {"singerName": "Sarala", "singerId": "sarala", "wikipediaUrl": ""},
    {"singerName": "TL Maharajan", "singerId": "tl_maharajan", "wikipediaUrl": "https://en.wikipedia.org/wiki/T._L._Maharajan"},
    {"singerName": "Kalyani Menon", "singerId": "kalyani_menon", "wikipediaUrl": "https://en.wikipedia.org/wiki/Kalyani_Menon"},
    {"singerName": "Baba Sehgal", "singerId": "baba_sehgal", "wikipediaUrl": "https://en.wikipedia.org/wiki/Baba_Sehgal"},
    {"singerName": "Uttara Kelkar", "singerId": "uttara_kelkar", "wikipediaUrl": "https://www.imdb.com/name/nm0445475/"},
    {"singerName": "Sudesh Bhonsle", "singerId": "sudesh_bhonsle", "wikipediaUrl": "https://en.wikipedia.org/wiki/Sudesh_Bhosale"},
    {"singerName": "Suresh Wadkar", "singerId": "suresh_wadkar", "wikipediaUrl": "https://en.wikipedia.org/wiki/Suresh_Wadkar"},
    {"singerName": "Anupama Deshapande", "singerId": "anupama_deshapande", "wikipediaUrl": "https://en.wikipedia.org/wiki/Anupama_Deshpande"},
    {"singerName": "Ravindra Satte", "singerId": "ravindra_satte", "wikipediaUrl": "https://en.wikipedia.org/wiki/Ravindra_Sathe"},
    {"singerName": "Bombay Saradha", "singerId": "bombay_saradha", "wikipediaUrl": ""},
    {"singerName": "Sivanesan", "singerId": "sivanesan", "wikipediaUrl": ""},
    {"singerName": "Ganga", "singerId": "ganga", "wikipediaUrl": ""},
    {"singerName": "Renuka", "singerId": "renuka", "wikipediaUrl": ""},
    {"singerName": "Anuradha Sriram", "singerId": "anuradha_sriram", "wikipediaUrl": "https://en.wikipedia.org/wiki/Anuradha_Sriram"},
    {"singerName": "Harini", "singerId": "harini", "wikipediaUrl": "https://en.wikipedia.org/wiki/Harini_(singer)"},
    {"singerName": "Sirkazhi Sivachidambaram", "singerId": "sirkazhi_sivachidambaram", "wikipediaUrl": "https://en.wikipedia.org/wiki/Sirkazhi_G._Sivachidambaram"},
    {"singerName": "Esther", "singerId": "esther", "wikipediaUrl": "https://en.wikipedia.org/wiki/Esther_Hnamte"},
    {"singerName": "Shwetha Mohan", "singerId": "shwetha_mohan", "wikipediaUrl": "https://en.wikipedia.org/wiki/Shweta_Mohan"},
    {"singerName": "Aditya Narayan", "singerId": "aditya_narayan", "wikipediaUrl": "https://en.wikipedia.org/wiki/Aditya_Narayan"},
    {"singerName": "Remo Fernandes", "singerId": "remo_fernandes", "wikipediaUrl": "https://en.wikipedia.org/wiki/Remo_Fernandes"},
    {"singerName": "Makummba", "singerId": "makummba", "wikipediaUrl": "https://www.discogs.com/artist/6029342-Makummba"},
    {"singerName": "Ila Arun", "singerId": "ila_arun", "wikipediaUrl": "https://en.wikipedia.org/wiki/Ila_Arun"},
    {"singerName": "Apache Indian", "singerId": "apache_indian", "wikipediaUrl": "https://en.wikipedia.org/wiki/Apache_Indian"},
    {"singerName": "Aslam Mustafa", "singerId": "aslam_mustafa", "wikipediaUrl": "https://www.imdb.com/name/nm2201775/"},
    {"singerName": "Sadhana Sargam", "singerId": "sadhana_sargam", "wikipediaUrl": "https://en.wikipedia.org/wiki/Sadhana_Sargam"},
    {"singerName": "Suchitra Krishnamoorthi", "singerId": "suchitra_krishnamoorthi", "wikipediaUrl": "https://en.wikipedia.org/wiki/Suchitra_Krishnamoorthi"},
    {"singerName": "Sumangali", "singerId": "sumangali", "wikipediaUrl": ""},
    {"singerName": "Dominique Cerejo", "singerId": "dominique_cerejo", "wikipediaUrl": "https://en.wikipedia.org/wiki/Dominique_Cerejo"},
    {"singerName": "Storms", "singerId": "storms", "wikipediaUrl": ""},
    {"singerName": "Rafee", "singerId": "rafee", "wikipediaUrl": ""},
    {"singerName": "OS Arun", "singerId": "os_arun", "wikipediaUrl": "https://osarun.in/"},
    {"singerName": "KK", "singerId": "kk", "wikipediaUrl": "https://en.wikipedia.org/wiki/KK_(singer)"},
    {"singerName": "Sonu Nigam", "singerId": "sonu_nigam", "wikipediaUrl": "https://en.wikipedia.org/wiki/Sonu_Nigam"},
    {"singerName": "Sangeetha Sajith", "singerId": "sangeetha_sajith", "wikipediaUrl": "https://en.wikipedia.org/wiki/Sangeetha_Sajith"},
    {"singerName": "Anto", "singerId": "anto", "wikipediaUrl": ""},
    {"singerName": "Chandran", "singerId": "chandran", "wikipediaUrl": ""},
    {"singerName": "Nagoor Mohammad Ali", "singerId": "nagoor_mohammad_ali", "wikipediaUrl": ""},
    {"singerName": "Raqueeb Alam", "singerId": "raqueeb_alam", "wikipediaUrl": ""},
    {"singerName": "Febi Mani", "singerId": "febi_mani", "wikipediaUrl": "https://en.wikipedia.org/wiki/Febi_Mani"},
    {"singerName": "Kavita Paudwal", "singerId": "kavita_paudwal", "wikipediaUrl": "https://en.wikipedia.org/wiki/Kavita_Paudwal"},
    {"singerName": "Arvind Swamy", "singerId": "arvind_swamy", "wikipediaUrl": "https://en.wikipedia.org/wiki/Arvind_Swamy"},
    {"singerName": "Sandhya Jayakrishna", "singerId": "sandhya_jayakrishna", "wikipediaUrl": "https://musicbrainz.org/artist/341ef75e-520f-4cfa-9ba5-815eb4350ce4"},
    {"singerName": "Bombay Jayashree", "singerId": "bombay_jayashree", "wikipediaUrl": "https://en.wikipedia.org/wiki/Bombay_Jayashri"},
    {"singerName": "Deena Chandra Das", "singerId": "deena_chandra_das", "wikipediaUrl": "https://en.wikipedia.org/wiki/Dheena_Chandra_Dhas"},
    {"singerName": "Ranu Mukherjee", "singerId": "ranu_mukherjee", "wikipediaUrl": ""},
    {"singerName": "Neeraj Vohra", "singerId": "neeraj_vohra", "wikipediaUrl": "https://en.wikipedia.org/wiki/Neeraj_Vora"},
    {"singerName": "Vinod Rathod", "singerId": "vinod_rathod", "wikipediaUrl": "https://en.wikipedia.org/wiki/Vinod_Rathod"},
    {"singerName": "Usha Uthup", "singerId": "usha_uthup", "wikipediaUrl": "https://en.wikipedia.org/wiki/Usha_Uthup"},
    {"singerName": "Srinivasa Murthy", "singerId": "srinivasa_murthy", "wikipediaUrl": "https://en.wikipedia.org/wiki/Srinivasa_Murthy"},
    {"singerName": "Hema Sardesai", "singerId": "hema_sardesai", "wikipediaUrl": "https://en.wikipedia.org/wiki/Hema_Sardesai"},
    {"singerName": "Abhijeet Bhattacharya", "singerId": "abhijeet_bhattacharya", "wikipediaUrl": "https://en.wikipedia.org/wiki/Abhijeet_Bhattacharya"},
    {"singerName": "Sukhwinder Singh", "singerId": "sukhwinder_singh", "wikipediaUrl": "https://en.wikipedia.org/wiki/Sukhwinder_Singh"},
    {"singerName": "Rangan", "singerId": "rangan", "wikipediaUrl": ""},
    {"singerName": "Ravi Kote", "singerId": "ravi_kote", "wikipediaUrl": ""},
    {"singerName": "Kumar Sanu", "singerId": "kumar_sanu", "wikipediaUrl": "https://en.wikipedia.org/wiki/Kumar_Sanu"},
    {"singerName": "Prabhakar", "singerId": "prabhakar", "wikipediaUrl": ""},
    {"singerName": "Krishnaraj", "singerId": "krishnaraj", "wikipediaUrl": ""},
    {"singerName": "Nithyasree", "singerId": "nithyasree", "wikipediaUrl": "https://en.wikipedia.org/wiki/Nithyasree_Mahadevan"},
    {"singerName": "Sapna Awasthi", "singerId": "sapna_awasthi", "wikipediaUrl": "https://en.wikipedia.org/wiki/Sapna_Awasthi"},
    {"singerName": "Lata Mangeshkar", "singerId": "lata_mangeshkar", "wikipediaUrl": "https://en.wikipedia.org/wiki/Lata_Mangeshkar"},
    {"singerName": "Mahalakshmi Iyer", "singerId": "mahalakshmi_iyer", "wikipediaUrl": "https://en.wikipedia.org/wiki/Mahalakshmi_Iyer"},
    {"singerName": "Palakkad Sriram", "singerId": "palakkad_sriram", "wikipediaUrl": "https://en.wikipedia.org/wiki/Palakkad_Sreeram"},
    {"singerName": "Sujata Trivedi", "singerId": "sujata_trivedi", "wikipediaUrl": "https://www.imdb.com/name/nm1242414/"},
    {"singerName": "Babul Supriyo", "singerId": "babul_supriyo", "wikipediaUrl": "https://en.wikipedia.org/wiki/Babul_Supriyo"},
    {"singerName": "Anuradha Paudwal", "singerId": "anuradha_paudwal", "wikipediaUrl": "https://en.wikipedia.org/wiki/Anuradha_Paudwal"},
    {"singerName": "Renu Mukherjee", "singerId": "renu_mukherjee", "wikipediaUrl": ""},
    {"singerName": "Chithra Srinivasan", "singerId": "chithra_srinivasan", "wikipediaUrl": ""},
    {"singerName": "Srilekha", "singerId": "srilekha", "wikipediaUrl": "https://en.wikipedia.org/wiki/Srilekha_Parthasarathy"},
    {"singerName": "Meherdeen", "singerId": "meherdeen", "wikipediaUrl": ""},
    {"singerName": "Pushpavanam Kuppusamy", "singerId": "pushpavanam_kuppusamy", "wikipediaUrl": "https://en.wikipedia.org/wiki/Pushpavanam_Kuppusamy"},
    {"singerName": "Ambili", "singerId": "ambili", "wikipediaUrl": "https://en.wikipedia.org/wiki/Ambili_(singer)"},
    {"singerName": "Devan Ekambaram", "singerId": "devan_ekambaram", "wikipediaUrl": "https://en.wikipedia.org/wiki/Devan_Ekambaram"},
    {"singerName": "Yugendran", "singerId": "yugendran", "wikipediaUrl": "https://en.wikipedia.org/wiki/Yugendran"},
    {"singerName": "MS Viswanathan", "singerId": "ms_viswanathan", "wikipediaUrl": "https://en.wikipedia.org/wiki/M._S._Viswanathan"},
    {"singerName": "Richa Sharma", "singerId": "richa_sharma", "wikipediaUrl": "https://en.wikipedia.org/wiki/Richa_Sharma_(singer)"},
    {"singerName": "Madhushree", "singerId": "madhushree", "wikipediaUrl": "https://en.wikipedia.org/wiki/Madhushree"},
    {"singerName": "Vaishali", "singerId": "vaishali", "wikipediaUrl": "https://en.wikipedia.org/wiki/Vaishali_Samant"},
    {"singerName": "Shoma", "singerId": "shoma", "wikipediaUrl": ""},
    {"singerName": "Deepika", "singerId": "deepika", "wikipediaUrl": ""},
    {"singerName": "Timmy", "singerId": "timmy", "wikipediaUrl": ""},
    {"singerName": "Rafi", "singerId": "rafi", "wikipediaUrl": ""},
    {"singerName": "Kalpana Raghavendar", "singerId": "kalpana_raghavendar", "wikipediaUrl": "https://en.wikipedia.org/wiki/Kalpana_Raghavendar"},
    {"singerName": "Clinton Cerejo", "singerId": "clinton_cerejo", "wikipediaUrl": "https://en.wikipedia.org/wiki/Clinton_Cerejo"},
    {"singerName": "Raihanah Shekar", "singerId": "raihanah_shekar", "wikipediaUrl": "https://en.wikipedia.org/wiki/A._R._Reihana"},
    {"singerName": "Feji", "singerId": "feji", "wikipediaUrl": ""},
    {"singerName": "Manoj Bharathiraja", "singerId": "manoj_bharathiraja", "wikipediaUrl": "https://en.wikipedia.org/wiki/Manoj_Bharathiraja"},
    {"singerName": "Arundathi", "singerId": "arundathi", "wikipediaUrl": "https://en.wikipedia.org/wiki/B._Arundhathi"},
    {"singerName": "Vasundara Das", "singerId": "vasundara_das", "wikipediaUrl": "https://en.wikipedia.org/wiki/Vasundhara_Das"},
    {"singerName": "Pravin Mani", "singerId": "pravin_mani", "wikipediaUrl": "https://en.wikipedia.org/wiki/Pravin_Mani"},
    {"singerName": "Roop Kumar Rathod", "singerId": "roop_kumar_rathod", "wikipediaUrl": "https://en.wikipedia.org/wiki/Roopkumar_Rathod"},
    {"singerName": "Surjo Bhattacharya", "singerId": "surjo_bhattacharya", "wikipediaUrl": "https://www.imdb.com/name/nm1240912/"},
    {"singerName": "Alisha Chinai", "singerId": "alisha_chinai", "wikipediaUrl": "https://en.wikipedia.org/wiki/Alisha_Chinai"},
    {"singerName": "SPB Charan", "singerId": "spb_charan", "wikipediaUrl": "https://en.wikipedia.org/wiki/S._P._Charan"},
    {"singerName": "Naveen", "singerId": "naveen", "wikipediaUrl": "https://www.imdb.com/name/nm3854718/"},
    {"singerName": "Neyveli Ramalakshmi", "singerId": "neyveli_ramalakshmi", "wikipediaUrl": "https://sukadhwani.wixsite.com/sukadhwani1/neyveliramalakshmi"},
    {"singerName": "Ustad Sultan Khan", "singerId": "ustad_sultan_khan", "wikipediaUrl": "https://en.wikipedia.org/wiki/Sultan_Khan_(musician)"},
    {"singerName": "Qadir Ghulam Mustafa", "singerId": "qadir_ghulam_mustafa", "wikipediaUrl": "https://en.wikipedia.org/wiki/Ghulam_Mustafa_Khan_(singer)"},
    {"singerName": "Murtaza Ghulam Mustafa", "singerId": "murtaza_ghulam_mustafa", "wikipediaUrl": ""},
    {"singerName": "Kamal Haasan", "singerId": "kamal_haasan", "wikipediaUrl": "https://en.wikipedia.org/wiki/Kamal_Haasan"},
    {"singerName": "Chithra Sivaraman", "singerId": "chithra_sivaraman", "wikipediaUrl": "https://en.wikipedia.org/wiki/Chitra_Iyer"},
    {"singerName": "Gopika Poornima", "singerId": "gopika_poornima", "wikipediaUrl": "https://en.wikipedia.org/wiki/Gopika_Poornima"},
    {"singerName": "Siloni Rath", "singerId": "siloni_rath", "wikipediaUrl": ""},
    {"singerName": "Sharanya Srinivas", "singerId": "sharanya_srinivas", "wikipediaUrl": "https://en.wikipedia.org/wiki/Sharanya_Srinivas"},
    {"singerName": "SP Sailaja", "singerId": "sp_sailaja", "wikipediaUrl": "https://en.wikipedia.org/wiki/S._P._Sailaja"},
    {"singerName": "Parthasarathy", "singerId": "parthasarathy", "wikipediaUrl": ""},
    {"singerName": "Poonam Bhatia", "singerId": "poonam_bhatia", "wikipediaUrl": ""},
    {"singerName": "Rageshwari", "singerId": "rageshwari", "wikipediaUrl": "https://en.wikipedia.org/wiki/Raageshwari_Loomba"},
    {"singerName": "Shaan", "singerId": "shaan", "wikipediaUrl": "https://en.wikipedia.org/wiki/Shaan_(singer)"},
    {"singerName": "Kishori Gowarikar", "singerId": "kishori_gowarikar", "wikipediaUrl": "https://www.imdb.com/name/nm1029773/"},
    {"singerName": "Karthik", "singerId": "karthik", "wikipediaUrl": "https://en.wikipedia.org/wiki/Karthik_(singer)"},
    {"singerName": "Balram", "singerId": "balram", "wikipediaUrl": ""},
    {"singerName": "Sriram Parthasarathy", "singerId": "sriram_parthasarathy", "wikipediaUrl": "https://en.wikipedia.org/wiki/Sriram_Parthasarathy"},
    {"singerName": "Sivamani", "singerId": "sivamani", "wikipediaUrl": "https://en.wikipedia.org/wiki/Sivamani_(percussionist)"},
    {"singerName": "Rashid Ali", "singerId": "rashid_ali", "wikipediaUrl": "https://en.wikipedia.org/wiki/Rashid_Ali_(singer)"},
    {"singerName": "Thubara", "singerId": "thubara", "wikipediaUrl": ""},
    {"singerName": "Sriram Narayanan", "singerId": "sriram_narayanan", "wikipediaUrl": "https://en.wikipedia.org/wiki/Palakkad_Sreeram"},
    {"singerName": "Tippu", "singerId": "tippu", "wikipediaUrl": "https://en.wikipedia.org/wiki/Tippu_(singer)"},
    {"singerName": "Srimathumitha", "singerId": "srimathumitha", "wikipediaUrl": "https://en.wikipedia.org/wiki/Srimathumitha"},
    {"singerName": "Mohammad Rafeeq", "singerId": "mohammad_rafeeq", "wikipediaUrl": ""},
    {"singerName": "ManikkaVinayagam", "singerId": "manikkavinayagam", "wikipediaUrl": "https://en.wikipedia.org/wiki/Manikka_Vinayagam"},
    {"singerName": "Chinmayi", "singerId": "chinmayi", "wikipediaUrl": "https://en.wikipedia.org/wiki/Chinmayi_Sripada"},
    {"singerName": "Manmohan Waris", "singerId": "manmohan_waris", "wikipediaUrl": "https://en.wikipedia.org/wiki/Manmohan_Waris"},
    {"singerName": "Reena Bhardwaj", "singerId": "reena_bhardwaj", "wikipediaUrl": "https://en.wikipedia.org/wiki/Reena_Bhardwaj"},
    {"singerName": "Blaaze", "singerId": "blaaze", "wikipediaUrl": "https://en.wikipedia.org/wiki/Blaaze"},
    {"singerName": "TR Silambarasan", "singerId": "tr_silambarasan", "wikipediaUrl": "https://en.wikipedia.org/wiki/Silambarasan"},
    {"singerName": "Adnan Sami", "singerId": "adnan_sami", "wikipediaUrl": "https://en.wikipedia.org/wiki/Adnan_Sami"},
    {"singerName": "Kunal Ganjawala", "singerId": "kunal_ganjawala", "wikipediaUrl": "https://en.wikipedia.org/wiki/Kunal_Ganjawala"}
]

def create_singer_payload():
    """
    Create a payload for adding a new singer to Contentful.
    
    :param singer_name: The name of the singer to be added.
    :return: A dictionary representing the singer entry payload.
    """

    for singer in singer_data:
        singer_id = singer.get('singerId', '').lower()
        singer_name = singer.get('singerName', '')
        wikipedia_url = singer.get('wikipediaUrl', '')

        entry_attributes = {
            'content_type_id': 'singer',
            'fields': { 
                'singerId': {
                    'en-US':singer_id
                },
                'singerName': {
                    'en-US': singer_name
                },
                'wikipediaUrl': {
                    'en-US': wikipedia_url
                }
            }
        }

        singer_entry = create_entry(singer_id, entry_attributes)
        print(f"Created entry for {singer_name} with ID: {singer_id}")
        

    

