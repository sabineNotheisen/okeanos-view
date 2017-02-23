def get_adherent_table():
    return '''
        id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
        type_id INTEGER,
        nom VARCHAR(100),
        prenom VARCHAR(100),
        email VARCHAR(255),
        tel VARCHAR(20),
        adress VARCHAR(100),
        cp INT(11),
        ville VARCHAR(50),
        num_licence VARCHAR(20),
        tel_accident VARCHAR(20),
        niveau_actuel VARCHAR(20),
        niveau_prepare VARCHAR(20),
        date_naissance DATE,
        date_certificat DATE,
        materiel INT(1),
        formation INT(1),
        attestation INT(1),
        tarif SMALLINT(6),
        FOREIGN KEY (type_id) REFERENCES type_of_adherent(id)
    '''


def get_type_of_adherent_table():
    return '''
        id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
        type VARCHAR(50)
    '''
