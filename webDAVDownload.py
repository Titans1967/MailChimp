from webdav3.client import Client
options = {
    'webdav_hostname': "https://skystorage.iscorp.com",
    'webdav_login': "skystorage\TrinityBasinTX",
    'webdav_password': "STRin3m3up"
}
client = Client(options)
client.download_sync("/TrinityBasinTX/MailChimp_import.xlsx", local_path=r"\\tb\shares\Bolt\Marketing Drive\MailChimp_import.xlsx")
