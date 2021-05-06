import datetime, random, string
import errno
import os
from OpenSSL import crypto
import base64
import xml.etree.ElementTree as ET
from io import BytesIO
from dataclasses import dataclass
import signxml
from signxml import XMLSigner, XMLVerifier

class FileNotPrivateKey(Exception):
    def __init__(self, message="You have to use private key(*.pem)"):
        self.message = message
        super().__init__(self.message)

class AltCurrencyAmountNullException(Exception):
    def __init__(self, message="Currency or amount is null"):
        self.message = message
        super().__init__(self.message)

@dataclass(frozen=True, order=True)
class MPIEnrolRequest:
    merchant_id: str
    terminal_id: str
    total_amount: str
    currency: str
    order_id: str
    purchase_desc: str
    card_num: str
    exp_year: str
    exp_month: str
    device_category: str = "0"

    def generate_xml(self, private_key) -> str:
        ECommerceConnect = ET.Element('ECommerceConnect')
        ECommerceConnect.set('xmlns:xenc', 'http://www.w3.org/2001/04/xmlenc#')
        ECommerceConnect.set('xmlns:ds', 'http://www.w3.org/2000/09/xmldsig#')
        ECommerceConnect.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        ECommerceConnect.set('xsi:noNamespaceSchemaLocation', 'https://secure.upc.ua/go/pub/schema/xmlpay-1.2.xsd')
        Message = ET.SubElement(ECommerceConnect, 'Message')
        Message.set('id', self.order_id)
        Message.set('version', '1.0')
        XMLMPIRequest = ET.SubElement(Message, 'XMLMPIRequest')
        MerchantID = ET.SubElement(XMLMPIRequest, 'MerchantID')
        MerchantID.text = self.merchant_id
        TerminalID = ET.SubElement(XMLMPIRequest, 'TerminalID')
        TerminalID.text = self.terminal_id
        MPIRequest = ET.SubElement(XMLMPIRequest, 'MPIRequest')
        MPIRequest.set('id', self.order_id)
        MPIEnrolRequest_node = ET.SubElement(MPIRequest, 'MPIEnrolRequest')
        CardNum = ET.SubElement(MPIEnrolRequest_node, 'CardNum')
        CardNum.text = self.card_num
        ExpYear = ET.SubElement(MPIEnrolRequest_node, 'ExpYear')
        ExpYear.text = self.exp_year
        ExpMonth = ET.SubElement(MPIEnrolRequest_node, 'ExpMonth')
        ExpMonth.text = self.exp_month
        TotalAmount = ET.SubElement(MPIEnrolRequest_node, 'TotalAmount')
        TotalAmount.text = self.total_amount
        Currency = ET.SubElement(MPIEnrolRequest_node, 'Currency')
        Currency.text = self.currency
        Description = ET.SubElement(MPIEnrolRequest_node, 'Description')
        Description.text = self.purchase_desc
        DeviceCategory = ET.SubElement(MPIEnrolRequest_node, 'DeviceCategory')
        DeviceCategory.text = self.device_category

        Signature = ET.SubElement(ECommerceConnect, 'Signature')

        if os.path.exists(private_key): 
            key_id = open(private_key).read();
            if key_id.startswith('-----BEGIN RSA PRIVATE KEY'):
                signed_root = XMLSigner(method=signxml.methods.enveloped,signature_algorithm='rsa-sha1',digest_algorithm="sha1").sign(ECommerceConnect, key=key_id)
        
        return ET.tostring(signed_root, encoding='UTF-8', method='xml')

    def generate_signature(self, private_key, element: ET) -> str:

        return 'to do'
        
@dataclass(frozen=True, order=True)
class Authorization:
    merchant_id: str
    terminal_id: str
    total_amount: str
    currency: str
    order_id: str
    purchase_desc: str
    card_num: str
    exp_year: str
    exp_month: str

    def generate_xml(self) -> str:
        ECommerceConnect = ET.Element('ECommerceConnect')
        ECommerceConnect.set('xmlns:xenc', 'http://www.w3.org/2001/04/xmlenc#')
        ECommerceConnect.set('xmlns:ds', 'http://www.w3.org/2000/09/xmldsig#')
        ECommerceConnect.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        ECommerceConnect.set('xsi:noNamespaceSchemaLocation', 'https://secure.upc.ua/go/pub/schema/xmlpay-1.2.xsd')
        Message = ET.SubElement(ECommerceConnect, 'Message')
        Message.set('id', self.order_id)
        return ET.tostring(ECommerceConnect, encoding='UTF-8', method='xml')