from crccheck.crc import CrcKermit

class FW_Data_Packet:
    def __init__(self, chunk, id):
        self.length = len(chunk) + 6
        self.id = id
        self.data = chunk
        self.crc = CrcKermit.calc(self.data)

    def lengthf(self):
        length = hex(self.length)[2:].zfill(4)
        length = bytes([int(length[2:], 16), int(length[:2], 16)])
        return length

    def idf(self):
        id = hex(self.id)[2:].zfill(4)
        id = bytes([int(id[2:], 16), int(id[:2], 16)])
        return id
    
    def crcf(self):
        crc = hex(self.crc)[2:].zfill(4)
        crc = bytes([int(crc[2:], 16), int(crc[:2], 16)])
        return crc
    
    def format(self):
        return self.lengthf() + self.idf() + self.data +self.crcf()
    
    def __repr__(self):
        return f'[FW_Data_Packet] <id:{self.id} data:{len(self.data)} bytes crc:{self.crc}>'
        
if __name__ == '__main__':
    b = bytes.fromhex('D7323566071624373301306FE0656754220E073311333801515F5140687A4040784E00647200245E79370175666772457713003501777A01D5507803712D522A422F357673352637E1FF306F941A645446AB0733D1E338012D885140D5CE404067FB00641163245E04DA0175606672454913003562147A0143517803532D522A042A3576291624370101306F4AF36754A8730433518F380169A451400B19404081F00264A5D3245E7E59017560667245491300358C187A0143517803532D522A042A3576291624370101306F6DF065AC779D81CB4CF0A8E90830D304EB3EEAB17949DA2173D124AE02CFAE870A0BC8AD257013C5007862BEDB283BF3314D4A6D9BCD367676F0273768267F9F6D0C77AC765614C3415430BE18C4500B756B48FF68B6013F161E218E69CF001E671B73BD2B1BF9E41287720E3E8D68FB3105FF366B523CA7276B7C88639A31A497D562B46395065847A8396A6522A895F9389693080900647223247A79120153133F5AFA52B1FBED537052BE10F330BC3B2E226D01600286E4F5275F796818D02CF0E755134435C3BDD54D283ACCA9C5105372B013C8E44D40F008D81A1E3285FB86016C1980FDB601570A463F874EF3EFB161DA00B531764A55241657923A902D1C0734774D071273A0D6FFE85C4EFD78CF50FD4BBE7C996346DBA99EC80185BDFC41B5808D0381FE8088FE238E4BF39BB3522A')
    p = FW_Data_Packet(b, 1)