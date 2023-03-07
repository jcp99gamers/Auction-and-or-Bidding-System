import os
import pathlib as pb
import firebase_admin
from firebase_admin import credentials, firestore

class FirebaseConnector():
    def __init__(self) -> None:
        path = pb.Path(__file__).parent.resolve().as_posix() #Used for Python Files
        self.FilePath = path + r"/serviceAccountKey.json"
    def ServiceKeyChecker(self):
        #JSON File & it's Path
        jsonWriter = open(self.FilePath,"w+")
        jsonWriter.write('{\n')
        jsonWriter.write('  '+'"type": "service_account",\n')
        jsonWriter.write('  '+'"project_id": "auction-bidding-arjun-gupta",\n')
        jsonWriter.write('  '+'"private_key_id": "337a0161999584d4f5bb4f520f960a5ec63ba961",\n')
        jsonWriter.write('  '+'"private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCyB7LNuG7apTjm\\nTSYmZlXrb1OOBau38lZwLoZkB9Z+mWfYpGfEIywAj9MiCWPRQZpywC3EpiX1zFOP\\neXaBa4P46X+T5kRIyq4MsAdg5HO3iP6o0YrtFsBn7Ij+qypfvs4xpzSQ4Jj7VHxr\\nKsyXRoWxA9tYEpqIR0N++KqPVSlk0bBDUBws+DvH2rymG1lyuSxScHOiLY6ZUX8z\\n7BFY1/GpYjPq0CaAYB4nqyV6Qg2AXivWnK8bEkEdoVGzrpWYilmfTdiVXg6Zwj/o\\njT2+V69CYvq6IkKFfUdje0Bgw+CamU0Ws1insoFyiwObuOIpMEt23gHEGPMn1cIX\\nOdoX4ZqdAgMBAAECggEADqzUSCFxH9xZP6Cx6Z3rbLQZUN52THwxNF+da976hyaJ\\nmSHaPOCCVsyERKy9+eicvONLEof4npWYeL30LxBoCUtkHRKw48gzRy/2d731LPah\\nuVRGjasfsqFcnJOK82gE0rJ8AopFCgipleLqCPlC+Xe+K7ki3GN1dKC2XIjSV/FO\\nz/D08Yg16MEoIMCZGiPotLmQcaVE+g7BsXg/v46QyyCgyDukjkWWJumilambVIRG\\nOuVo5tAf3TPI1hk2VEZk53gI3APEnH8KuN3rsXTgZQY9C82DqZjZUgctXxu0gnGR\\nImP1GLyFmUxVte4DiT1l5Mrc5pzDYZiNyRLhZ2kEkQKBgQDaiCbdZmPxfvlckf3E\\nDwxAFPlSODUO0bp6+bwdcp9ADFk4KFJvKhQU4j2QNiARfrrgTFAgcPjOkeYxfUvu\\n8Hn2HX55egBIFG5O4RviKnIHPIajWnteXZROmKqU+NK0uSRNqIjuqvxex21CKef8\\nNnYAPaEbgGHN5A50tTvqRcOMMQKBgQDQjdV7K/tHN85LpZ7aJj+qfsbE8196hBZD\\nohNeHbiiv4yDHgknC7O8Yn+mVdW23KigWB7oqrDFhJqarfdAEx0vzUENAWRPGm0I\\n56mgss1pqllMmlOrFYLhCH2CS6jsX8n1zQH7KXOfb9NYQVDh0DuMmQIO+8j2sHog\\nD/G2OyHWLQKBgDairZzS2Y/qH+v98AURgg2PcNoWhWVkGAxg3aA7JQd9Tt0Ub6+t\\nRIIIIj4o2hGlrpEfYzUJKZtzrKqY2eAuLT/UFefHEcTznrSH4VHFLOcUQdEbcRah\\nrM+NqbA/GWbnluT3iuyowRntICrXkVFkSFI9Fkdq7IjuSJLzMLycnowxAoGBALmh\\n5alzJoDnvWo8Cz8l2HmLyqU38357381nkFGvps7GLO3waDknA17lVbXapRXVJwtC\\nJJD4jcviEjMoMfIIkWwhCIvo9z4pyW+ptKTjQk+RX1b97wdTaGGhSwYVDlEHmh59\\n0gubg90gjj/6M2IsFTU6ZEit+N0LjEjJqF6KF74pAoGADrAvgFG9k4XvgOusCzoa\\nB7x+Ih2B70w2jhQHRXN2EzExHmSdf4xKK/31jBnwK/NkG/r7CBnALo63WkQYSrmZ\\nsL1x3NA2oiPYUXrSY4k6Y0631yak93jB/RNLFjT4TQWv8Sl9/fYZvnnNDXTEaQfP\\ncXvbY4iB8Cfnp5U4d3YJzKw=\\n-----END PRIVATE KEY-----\\n",\n')
        jsonWriter.write('  '+'"client_email": "firebase-adminsdk-mdv94@auction-bidding-arjun-gupta.iam.gserviceaccount.com",\n')
        jsonWriter.write('  '+'"client_id": "103080961495834562053",\n')
        jsonWriter.write('  '+'"auth_uri": "https://accounts.google.com/o/oauth2/auth",\n')
        jsonWriter.write('  '+'"token_uri": "https://oauth2.googleapis.com/token",\n')
        jsonWriter.write('  '+'"auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",\n')
        jsonWriter.write('  '+'"client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-mdv94%40auction-bidding-arjun-gupta.iam.gserviceaccount.com"\n')
        jsonWriter.write('}')
        jsonWriter.close()
        # # time.sleep(5)
        # pATH = r'{}'.format(os.getcwd())
        # fILE = r"\serviceAccountKey.json"
    def FirestoreConnector(self):
        #Initialize & Authenticate a Database
        try:
            app = firebase_admin.get_app()
        except ValueError as e:
            cred = credentials.Certificate(self.FilePath)
            firebase_admin.initialize_app(cred)
        #Connect to Firestore
        db = firestore.client()  # this connects to our Firestore database
        return db