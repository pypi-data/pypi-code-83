from typing import Any  # noqa
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field
from typing_extensions import Literal


class AppointmentResponseSchema(BaseModel):
    center_id: "float" = Field(..., alias="center_id")
    name: "str" = Field(..., alias="name")
    name_l: "Optional[str]" = Field(None, alias="name_l")
    state_name: "str" = Field(..., alias="state_name")
    state_name_l: "Optional[str]" = Field(None, alias="state_name_l")
    district_name: "str" = Field(..., alias="district_name")
    district_name_l: "Optional[str]" = Field(None, alias="district_name_l")
    block_name: "str" = Field(..., alias="block_name")
    block_name_l: "Optional[str]" = Field(None, alias="block_name_l")
    pincode: "str" = Field(..., alias="pincode")
    lat: "Optional[float]" = Field(None, alias="lat")
    long: "Optional[float]" = Field(None, alias="long")
    _from: "str" = Field(..., alias="from")
    to: "str" = Field(..., alias="to")
    fee_type: "Literal['Free', 'Paid']" = Field(..., alias="fee_type")
    dose: "float" = Field(..., alias="dose")
    appointment_id: "UUID" = Field(..., alias="appointment_id")
    session_id: "UUID" = Field(..., alias="session_id")
    date: "str" = Field(..., alias="date")
    slot: "str" = Field(..., alias="slot")


class AppointmentResponseSchemaAllOf(BaseModel):
    dose: "float" = Field(..., alias="dose")
    appointment_id: "UUID" = Field(..., alias="appointment_id")
    session_id: "UUID" = Field(..., alias="session_id")
    date: "str" = Field(..., alias="date")
    slot: "str" = Field(..., alias="slot")


class BenefeiciaryResponseSchema(BaseModel):
    beneficiary_reference_id: "str" = Field(..., alias="beneficiary_reference_id")
    name: "str" = Field(..., alias="name")
    birth_year: "str" = Field(..., alias="birth_year")
    gender: "str" = Field(..., alias="gender")
    mobile_number: "str" = Field(..., alias="mobile_number")
    photo_id_type: "str" = Field(..., alias="photo_id_type")
    photo_id_number: "str" = Field(..., alias="photo_id_number")
    comorbidity_ind: "Literal['Y', 'N']" = Field(..., alias="comorbidity_ind")
    vaccination_status: "Literal['Not Vaccinated', 'Partially Vaccinated', 'Vaccinated']" = Field(
        None, alias="vaccination_status"
    )
    vaccine: "Literal['COVISHIELD', 'COVAXIN']" = Field(None, alias="vaccine")
    dose1_date: "Optional[str]" = Field(None, alias="dose1_date")
    dose2_date: "Optional[str]" = Field(None, alias="dose2_date")
    appointments: "Optional[List[AppointmentResponseSchema]]" = Field(None, alias="appointments")


class CenterResponseSchema(BaseModel):
    center_id: "float" = Field(..., alias="center_id")
    name: "str" = Field(..., alias="name")
    name_l: "Optional[str]" = Field(None, alias="name_l")
    state_name: "str" = Field(..., alias="state_name")
    state_name_l: "Optional[str]" = Field(None, alias="state_name_l")
    district_name: "str" = Field(..., alias="district_name")
    district_name_l: "Optional[str]" = Field(None, alias="district_name_l")
    block_name: "str" = Field(..., alias="block_name")
    block_name_l: "Optional[str]" = Field(None, alias="block_name_l")
    pincode: "str" = Field(..., alias="pincode")
    lat: "Optional[float]" = Field(None, alias="lat")
    long: "Optional[float]" = Field(None, alias="long")
    _from: "str" = Field(..., alias="from")
    to: "str" = Field(..., alias="to")
    fee_type: "Literal['Free', 'Paid']" = Field(..., alias="fee_type")


class InlineObject(BaseModel):
    mobile: "Optional[str]" = Field(None, alias="mobile")


class InlineObject1(BaseModel):
    otp: "Optional[str]" = Field(None, alias="otp")
    txn_id: "Optional[UUID]" = Field(None, alias="txnId")


class InlineObject2(BaseModel):
    mobile: "Optional[str]" = Field(None, alias="mobile")


class InlineObject3(BaseModel):
    otp: "Optional[str]" = Field(None, alias="otp")
    txn_id: "Optional[UUID]" = Field(None, alias="txnId")


class InlineObject4(BaseModel):
    name: "str" = Field(..., alias="name")
    birth_year: "str" = Field(..., alias="birth_year")
    gender_id: "Optional[float]" = Field(None, alias="gender_id")
    photo_id_type: "float" = Field(..., alias="photo_id_type")
    photo_id_number: "str" = Field(..., alias="photo_id_number")
    comorbidity_ind: "Literal['Y', 'N']" = Field(None, alias="comorbidity_ind")
    consent_version: "str" = Field(..., alias="consent_version")


class InlineObject5(BaseModel):
    beneficiary_reference_id: "Optional[str]" = Field(None, alias="beneficiary_reference_id")


class InlineObject6(BaseModel):
    dose: "Optional[float]" = Field(None, alias="dose")
    session_id: "UUID" = Field(..., alias="session_id")
    slot: "str" = Field(..., alias="slot")
    beneficiaries: "List[str]" = Field(..., alias="beneficiaries")


class InlineObject7(BaseModel):
    appointment_id: "UUID" = Field(..., alias="appointment_id")
    session_id: "UUID" = Field(..., alias="session_id")
    slot: "str" = Field(..., alias="slot")


class InlineObject8(BaseModel):
    appointment_id: "UUID" = Field(..., alias="appointment_id")
    beneficiaries_to_cancel: "Optional[List[str]]" = Field(None, alias="beneficiariesToCancel")


class InlineResponse200(BaseModel):
    txn_id: "Optional[UUID]" = Field(None, alias="txnId")


class InlineResponse2001(BaseModel):
    token: "Optional[str]" = Field(None, alias="token")


class InlineResponse2002(BaseModel):
    states: "Optional[List[InlineResponse2002States]]" = Field(None, alias="states")
    ttl: "Optional[float]" = Field(None, alias="ttl")


class InlineResponse2002States(BaseModel):
    state_id: "float" = Field(..., alias="state_id")
    state_name: "str" = Field(..., alias="state_name")
    state_name_l: "Optional[str]" = Field(None, alias="state_name_l")


class InlineResponse2003(BaseModel):
    districts: "Optional[List[InlineResponse2003Districts]]" = Field(None, alias="districts")
    ttl: "Optional[float]" = Field(None, alias="ttl")


class InlineResponse2003Districts(BaseModel):
    state_id: "Optional[float]" = Field(None, alias="state_id")
    district_id: "float" = Field(..., alias="district_id")
    district_name: "str" = Field(..., alias="district_name")
    district_name_l: "Optional[str]" = Field(None, alias="district_name_l")


class InlineResponse2004(BaseModel):
    token: "Optional[str]" = Field(None, alias="token")
    is_new_account: "Literal['Y', 'N']" = Field(None, alias="isNewAccount")


class InlineResponse2005(BaseModel):
    types: "Optional[List[InlineResponse2005Types]]" = Field(None, alias="types")
    ttl: "Optional[float]" = Field(None, alias="ttl")


class InlineResponse2005Types(BaseModel):
    type: "str" = Field(..., alias="type")
    type_l: "Optional[str]" = Field(None, alias="type_l")
    id: "float" = Field(..., alias="id")


class InlineResponse2006(BaseModel):
    genders: "Optional[List[InlineResponse2006Genders]]" = Field(None, alias="genders")
    ttl: "Optional[float]" = Field(None, alias="ttl")


class InlineResponse2006Genders(BaseModel):
    gender: "str" = Field(..., alias="gender")
    gender_l: "Optional[str]" = Field(None, alias="gender_l")
    id: "float" = Field(..., alias="id")


class InlineResponse2007(BaseModel):
    beneficiary_reference_id: "Optional[str]" = Field(None, alias="beneficiary_reference_id")


class InlineResponse400(BaseModel):
    error_code: "Optional[str]" = Field(None, alias="errorCode")
    error: "Optional[str]" = Field(None, alias="error")


class SessionCalendarEntrySchema(BaseModel):
    center_id: "float" = Field(..., alias="center_id")
    name: "str" = Field(..., alias="name")
    name_l: "Optional[str]" = Field(None, alias="name_l")
    state_name: "str" = Field(..., alias="state_name")
    state_name_l: "Optional[str]" = Field(None, alias="state_name_l")
    district_name: "str" = Field(..., alias="district_name")
    district_name_l: "Optional[str]" = Field(None, alias="district_name_l")
    block_name: "str" = Field(..., alias="block_name")
    block_name_l: "Optional[str]" = Field(None, alias="block_name_l")
    pincode: "str" = Field(..., alias="pincode")
    lat: "Optional[float]" = Field(None, alias="lat")
    long: "Optional[float]" = Field(None, alias="long")
    _from: "str" = Field(..., alias="from")
    to: "str" = Field(..., alias="to")
    fee_type: "Literal['Free', 'Paid']" = Field(..., alias="fee_type")
    vaccine_fees: "Optional[List[VaccineFeeSchema]]" = Field(None, alias="vaccine_fees")
    sessions: "List[SessionCalendarEntrySchemaSessions]" = Field(..., alias="sessions")


class SessionCalendarEntrySchemaSessions(BaseModel):
    session_id: "UUID" = Field(..., alias="session_id")
    date: "str" = Field(..., alias="date")
    available_capacity: "float" = Field(..., alias="available_capacity")
    min_age_limit: "float" = Field(..., alias="min_age_limit")
    vaccine: "str" = Field(..., alias="vaccine")
    slots: "List[str]" = Field(..., alias="slots")


class SessionResponseSchema(BaseModel):
    center_id: "float" = Field(..., alias="center_id")
    name: "str" = Field(..., alias="name")
    name_l: "Optional[str]" = Field(None, alias="name_l")
    state_name: "str" = Field(..., alias="state_name")
    state_name_l: "Optional[str]" = Field(None, alias="state_name_l")
    district_name: "str" = Field(..., alias="district_name")
    district_name_l: "Optional[str]" = Field(None, alias="district_name_l")
    block_name: "str" = Field(..., alias="block_name")
    block_name_l: "Optional[str]" = Field(None, alias="block_name_l")
    pincode: "str" = Field(..., alias="pincode")
    lat: "Optional[float]" = Field(None, alias="lat")
    long: "Optional[float]" = Field(None, alias="long")
    _from: "str" = Field(..., alias="from")
    to: "str" = Field(..., alias="to")
    fee_type: "Literal['Free', 'Paid']" = Field(..., alias="fee_type")
    fee: "str" = Field(..., alias="fee")
    session_id: "UUID" = Field(..., alias="session_id")
    date: "str" = Field(..., alias="date")
    available_capacity: "float" = Field(..., alias="available_capacity")
    min_age_limit: "float" = Field(..., alias="min_age_limit")
    vaccine: "str" = Field(..., alias="vaccine")
    slots: "List[str]" = Field(..., alias="slots")


class SessionResponseSchemaAllOf(BaseModel):
    fee: "str" = Field(..., alias="fee")
    session_id: "UUID" = Field(..., alias="session_id")
    date: "str" = Field(..., alias="date")
    available_capacity: "float" = Field(..., alias="available_capacity")
    min_age_limit: "float" = Field(..., alias="min_age_limit")
    vaccine: "str" = Field(..., alias="vaccine")
    slots: "List[str]" = Field(..., alias="slots")


class VaccineFeeSchema(BaseModel):
    vaccine: "str" = Field(..., alias="vaccine")
    fee: "str" = Field(..., alias="fee")
