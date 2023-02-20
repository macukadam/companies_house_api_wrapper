"""A very simple wrapper around Companies House api."""

import os
import requests
from dotenv import load_dotenv

load_dotenv()


class APIpaths():
    """API paths for Companies House api."""
    company = 'company'
    officers = 'officers'
    registers = 'registers'
    charges = 'charges'
    exemptions = 'exemptions'
    filing_history = 'filing-history'
    insolvency = 'insolvency'
    disqualifications_corporate = 'disqualified-officers/corporate'
    disqualifications_natulal = 'disqualified-officers/natural'
    uk_establishments = 'uk-establishments'
    persons_with_significant_control = 'persons-with-significant-control'
    persons_with_significant_control_statements = 'persons-with-significant-control-statements'
    super_secure = 'super-secure'
    super_secure_beneficial_owner = 'super-secure-beneficial-owner'
    legal_person = 'legal-person'
    legal_person_beneficial_owner = 'legal-person-beneficial-owner'
    individual = 'individual'
    individual_beneficial_owner = 'individual-beneficial-owner'
    corporate_entity = 'corporate-entity'
    corporate_entity_beneficial_owner = 'corporate-entity-beneficial-owner'
    appointments = 'appointments'
    advanced_company_search = 'advanced-search/companies'
    search_all = 'search'
    search_companies = 'search/companies'
    search_officers = 'search/officers'
    search_disqualified_officers = 'search/disqualified-officers'
    search_companies_alphabetically = 'alphabetic-search/companies'
    search_dissolved_companies = 'dissolved-search/companies'


class CompaniesHouse:
    """
    A class for interacting with the Companies House API.

    Raises:
    -----------
    ValueError: If the required environment variables are not set.

    Attributes:
    -----------
    host (str): The COMPANIES HOUSE API host URL.

    Example usage:
    -----------
        >>> ch = CompaniesHouse()
        >>> response = coc.get_company_profile('12345678')
    """

    def __init__(self) -> None:

        self.host = os.getenv('COMPANIES_HOUSE_HOST')
        self.api_key = os.getenv("COMPANIES_HOUSE_APIKEY")

        if not self.host:
            raise ValueError('KVK_HOST is not set')

        if not self.api_key:
            raise ValueError('KVK_APIKEY is not set')

        self.headers = {'Authorization': self.api_key}

    def __send_request(self, request_type, *res, **params) \
            -> requests.Response:

        if self.host is None:
            raise ValueError('HOST is not set')

        url = self.host + ''.join(['/' + r for r in res if r is not None])

        response = requests.request(
            request_type, url, headers=self.headers, params=params)

        return response

    def get_company_profile(self, company_number: str) -> requests.Response:
        """
        Get the basic company information

        :param company_number : The company number of the basic information to return.
        """

        response = self.__send_request(
            "GET", APIpaths.company, company_number)

        return response

    def advanced_company_search(self,
                                company_name_includes: str | None = None,
                                company_name_excludes: str | None = None,
                                company_status: str | None = None,
                                company_subtype: str | None = None,
                                company_type: str | None = None,
                                dissolved_from: str | None = None,
                                dissolved_to: str | None = None,
                                incorporated_from: str | None = None,
                                incorporated_to: str | None = None,
                                location: str | None = None,
                                sic_codes: str | None = None,
                                size: int | None = None,
                                start_index: int | None = None):
        """
        Perform an advanced search for companies using the Companies House API.

        :param company_name_includes: Filter by company name includes.
        :param company_name_excludes: Filter by company name excludes.
        :param company_status: Filter by company status. Use a comma delimited list or multiple of the same key to search using multiple values.
        :param company_subtype: Filter by company subtype. Use a comma delimited list or multiple of the same key to search using multiple values.
        :param company_type: Filter by company type. Use a comma delimited list or multiple of the same key to search using multiple values.
        :param dissolved_from: Filter by dissolved from date.
        :param dissolved_to: Filter by dissolved to date.
        :param incorporated_from: Filter by incorporated from date.
        :param incorporated_to: Filter by incorporated to date.
        :param location: Filter by company location.
        :param sic_codes: Filter by SIC codes. Use a comma delimited list or multiple of the same key to search using multiple values.
        :param size: Maximum number of results to return.
        :param start_index: Point at which results will start from.

        :return: A dictionary containing the search results, or None if the search was unsuccessful.
        """
        params = {
            'company_name_includes': company_name_includes,
            'company_name_excludes': company_name_excludes,
            'company_status': company_status,
            'company_subtype': company_subtype,
            'company_type': company_type,
            'dissolved_from': dissolved_from,
            'dissolved_to': dissolved_to,
            'incorporated_from': incorporated_from,
            'incorporated_to': incorporated_to,
            'location': location,
            'sic_codes': sic_codes,
            'size': size,
            'start_index': start_index
        }

        response = self.__send_request(
            "GET", APIpaths.advanced_company_search, **params)

        return response

    def search_all(self, q: str, items_per_page: int | None = None,
                   start_index: int | None = None) -> requests.Response:
        """
        Search companies, officers and disqualified officers

        :param q : The term being searched for.
        :param items_per_page : The number of items per page.
        :param start_index : The index at which to start the search.
        """

        params = {
            'q': q,
            'items_per_page': items_per_page,
            'start_index': start_index
        }

        response = self.__send_request(
            "GET", APIpaths.search_all, **params)

        return response

    def search_companies(self, q: str, items_per_page: int | None = None,
                         start_index: int | None = None,
                         restrictions: str | None = None) -> requests.Response:
        """
        Search company information

        :param q : The term being searched for.
        :param items_per_page : The number of search results to return per page.
        :param start_index : The index of the first result item to return.
        :param restrictions : Enumerable options to restrict search results. Space separate multiple restriction options to combine functionality. For a "company name availability" search use "active-companies legally-equivalent-company-name" together.
        """

        params = {
            'q': q,
            'items_per_page': items_per_page,
            'start_index': start_index,
            'restrictions': restrictions
        }

        response = self.__send_request(
            "GET", APIpaths.search_companies, **params)

        return response

    def search_officers(self, q: str, items_per_page: int | None = None,
                        start_index: int | None = None) -> requests.Response:
        """
        Search for officer information


        :param q : The term being searched for.
        :param items_per_page : The number of items per page.
        :param start_index : The index of the first result item to return.
        """

        params = {
            'q': q,
            'items_per_page': items_per_page,
            'start_index': start_index
        }

        response = self.__send_request(
            "GET", APIpaths.search_officers, **params)

        return response

    def search_disqualified_officers(self, q: str, items_per_page: int | None = None,
                                     start_index: int | None = None) -> requests.Response:
        """
        Search for disqualified officer information


        :param q : The term being searched for.
        :param items_per_page : The number of items per page.
        :param start_index : The start index.
        """

        params = {
            'q': q,
            'items_per_page': items_per_page,
            'start_index': start_index
        }

        response = self.__send_request(
            "GET", APIpaths.search_disqualified_officers, **params)

        return response

    def search_companies_alphabetically(self, q: str,
                                        search_above: str | None = None,
                                        search_below: str | None = None,
                                        size: str | None = None) -> requests.Response:
        """
        Sends a GET request to the Companies House and returns the response.

        :param q : The company name being searched for
        :param search_above : The ordered_alpha_key_with_id used for paging
        :param search_below : The ordered_alpha_key_with_id used for paging
        :param size: The maximum number of results matching the search term(s) to return with a range of 1 to 100
        """

        params = {
            'q': q,
            'search_above': search_above,
            'search_below': search_below,
            'size': size
        }

        response = self.__send_request(
            "GET", APIpaths.search_companies_alphabetically, **params)

        return response

    def search_dissolved_companies(self, q: str,
                                   search_type: str,
                                   search_above: str | None = None,
                                   search_below: str | None = None,
                                   size: str | None = None,
                                   start_index: int | None = None) -> requests.Response:
        """
        Search for a dissolved company

        :param q : The term being searched for.
        :param search_type Determines type of search. Options are alphabetical, best-match, previous-name-dissolved:
        :param search_above : The ordered_alpha_key_with_id used for paging
        :param search_below : The ordered_alpha_key_with_id used for paging
        :param size: The maximum number of results matching the search term(s) to return with a range of 1 to 100
        :param start_index: Used in best-match and previous-name-dissolved search-type
        """

        params = {
            'q': q,
            'search_type': search_type,
            'search_above': search_above,
            'search_below': search_below,
            'size': size,
            'start_index': start_index
        }

        response = self.__send_request(
            "GET", APIpaths.search_dissolved_companies, **params)

        return response

    def get_officers(self, company_number: str,
                     items_per_page: int | None = None,
                     register_type: str | None = None,
                     register_view: str | None = None,
                     start_index: int | None = None,
                     order_by: str | None = None) -> requests.Response:
        """
        Get officers for a company

        :param company_number : The company number of the officer list being requested..
        :param items_per_page : The number of officers to return per page.
        :param register_type: The register_type determines which officer type is returned for the registers view.The register_type field will only work if registers_view is set to true
            Possible values are:
            directors
            secretaries
            llp-members
        :param register_view: Display register specific information. If given register is held at Companies House, registers_view set to true and correct register_type specified, only active officers will be returned. Those will also have full date of birth.Defaults to false
            Possible values are:
            true
            false
        :param start_index : The offset into the entire result set that this page starts.
        :param order_by: The field by which to order the result set.
            Possible values are:
            appointed_on
            resigned_on
            surname
        """

        params = {
            'items_per_page': items_per_page,
            'register_type': register_type,
            'register_view': register_view,
            'start_index': start_index,
            'order_by': order_by
        }

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.officers, **params)

        return response

    def get_company_officer_appointment(self, company_number: str,
                                        officer_id: str,
                                        appointment_id: str) -> requests.Response:
        """
        Get details of an individual company officer appointment

        :param company_number : The company number of the officer list being requested..
        :param officer_id : The officer id of the officer appointment being requested.
        :param appointment_id : The appointment id of the officer appointment being requested.
        """

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.officers, officer_id,
            APIpaths.appointments, appointment_id)

        return response

    def get_company_registers(self, company_number: str) -> requests.Response:
        """
        Get the company registers information


        :param company_number : The company number of the register information to return.
        """

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.registers)

        return response

    def get_comapany_charges(self, company_number: str) -> requests.Response:
        """
        List of charges for a company.

        :param company_number : The company number that the charge list is required for.
        """

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.charges)

        return response

    def get_company_charge(self, company_number: str, charge_id: str) -> requests.Response:
        """
        Get a charge for a company.

        :param company_number : The company number that the charge list is required for.
        :param charge_id : The charge id that the charge is required for.
        """

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            company_number, APIpaths.charges, charge_id)

        return response

    def get_company_filing_history(self, company_number: str,
                                   category: str | None = None,
                                   items_per_page: int | None = None,
                                   start_index: int | None = None) -> requests.Response:
        """
        Get the filing history list of a company

        :param company_number : The company number that the filing history is required for.
        :param category : One or more comma-separated categories to filter by (inclusive).
        :param items_per_page : The number of filing history items to return per page.
        """

        params = {
            'category': category,
            'items_per_page': items_per_page,
            'start_index': start_index
        }

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.filing_history, **params)

        return response

    def get_company_filing_history_item(self, company_number: str,
                                        transaction_id: str) -> requests.Response:
        """
        Get the filing history item of a company

        :param company_number : The company number that the filing history is required for.
        :param transaction_id : The transaction id of the filing history item to return.
        """

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.filing_history, transaction_id)

        return response

    def get_company_insolvency_information(self, company_number: str) -> requests.Response:
        """
        Get the insolvency information of a company

        :param company_number : The company number of the basic information to return.
        """

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.insolvency)

        return response

    def get_company_exemptions_information(self, company_number: str) -> requests.Response:
        """
        Get the exemptions information of a company

        :param company_number : The company number of the basic information to return.
        """

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.exemptions)

        return response

    def get_cooporate_officer_disqualifications(self, officer_id: str) -> requests.Response:
        """
        Get a corporate officer's disqualifications

        :param officer_id : The officer id of the officer disqualifications to return.
        """

        response = self.__send_request(
            "GET", APIpaths.officers,
            APIpaths.disqualifications_corporate, officer_id)

        return response

    def get_natural_officer_disqualifications(self, officer_id: str) -> requests.Response:
        """
        Get a natural officer's disqualifications


        :param officer_id : The disqualified officer's id.
        """

        response = self.__send_request(
            "GET", APIpaths.officers,
            APIpaths.disqualifications_natulal, officer_id)

        return response

    def get_officer_appointments(self, officer_id: str, items_per_page: int | None = None,
                                 start_index: int | None = None) -> requests.Response:
        """
        Get a list of officer appointments

        :param officer_id : The officer id of the officer appointments to return.
        :param items_per_page : The number of officer appointments to return per page.
        :param start_index : The index of the first officer appointment to return.
        """

        params = {
            'items_per_page': items_per_page,
            'start_index': start_index
        }

        response = self.__send_request(
            "GET", APIpaths.officers, officer_id,
            APIpaths.appointments, **params)

        return response

    def get_company_uk_enstablishment(self, company_number: str) -> requests.Response:
        """
        Get list of uk-establishments companies


        :param company_number : Company number.

        """

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.uk_establishments)

        return response

    def get_persons_with_significant_control(self, company_number: str,
                                             items_per_page: str | None = None,
                                             start_index: str | None = None,
                                             register_view: str | None = None) -> requests.Response:
        """
        Get a list of persons with significant control

        :param company_number : The company number of the persons with significant control to return.
        :param items_per_page : The number of persons with significant control to return per page.
        :param start_index : The index of the first person with significant control to return.
        :param register_view: Display register specific information. If register is held at Companies House and register_view is set to true, only PSCs which are active or were terminated during election period are shown together with full dates of birth where available.
            Accepted values are:
                -true
                -false
            Defaults to false
        """

        params = {
            'items_per_page': items_per_page,
            'start_index': start_index,
            'register_view': register_view
        }

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.persons_with_significant_control, **params)

        return response

    def get_persons_with_significant_control_statements(self, company_number: str,
                                                        items_per_page: str | None = None,
                                                        start_index: str | None = None,
                                                        register_view: str | None = None) -> requests.Response:
        """
        Get a list of persons with significant control statements

        :param company_number : The company number of the persons with significant control statements to return.
        :param items_per_page : The number of persons with significant control statements to return per page.
        :param start_index : The index of the first person with significant control statement to return.
        :param register_view: Display register specific information. If register is held at Companies House and register_view is set to true, only PSCs which are active or were terminated during election period are shown together with full dates of birth where available.
            Accepted values are:
                -true
                -false
            Defaults to false
        """

        params = {
            'items_per_page': items_per_page,
            'start_index': start_index,
            'register_view': register_view
        }

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.persons_with_significant_control_statements, **params)

        return response

    def get_the_super_secure_person_with_significant_control(self, company_number: str,
                                                             super_secure_id) -> requests.Response:
        """
        Get details of a super secure person with significant control

        :param company_number : The company number of the super secure person with significant control details being requested..
        :param super_secure_id : The id of the super secure person with significant control details being requested.
        """

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.persons_with_significant_control, super_secure_id)

        return response

    def get_the_super_secure_beneficial_owner(self, company_number: str,
                                              super_secure_id) -> requests.Response:
        """
        Get details of a super secure person with significant control

        :param company_number : The company number of the super secure beneficial owner details being requested..
        :param super_secure_id : The id of the super secure beneficial owner details being requested.
        """

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.super_secure_beneficial_owner, super_secure_id)

        return response

    def get_person_with_significant_control_statement(self,
                                                      company_number: str,
                                                      statement_id: str) -> requests.Response:
        """
        Get details of a person with significant control statement

        :param company_number : The company number of the person with significant control statement details being requested..
        :param statement_id : The id of the person with significant control statement details being requested.
        """

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.persons_with_significant_control_statements,
            statement_id)

        return response

    def get_legal_person_with_significant_control(self, company_number: str,
                                                  psc_id: str) -> requests.Response:
        """
        Get details of a legal person with significant control

        :param company_number : The company number of the legal person with significant control details being requested..
        :param psc_id : The id of the legal person with significant control details being requested.
        """

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.persons_with_significant_control,
            APIpaths.legal_person, psc_id)

        return response

    def get_legal_person_beneficial_owner(self, company_number: str,
                                          psc_id: str) -> requests.Response:
        """
        Get details of a legal person beneficial owner

        :param company_number : The company number of the legal person beneficial owner details being requested..
        :param psc_id : The id of the legal person beneficial owner details being requested.
        """

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.persons_with_significant_control,
            APIpaths.legal_person_beneficial_owner, psc_id)

        return response

    def get_individual_person_with_significant_control(self, company_number: str,
                                                       psc_id: str) -> requests.Response:
        """
        Get details of an individual person with significant control

        :param company_number : The company number of the individual person with significant control details being requested..
        :param psc_id : The id of the individual person with significant control details being requested.
        """

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.persons_with_significant_control,
            APIpaths.individual, psc_id)

        return response

    def get_individual_beneficial_owner(self, company_number: str,
                                        psc_id: str) -> requests.Response:
        """
        Get details of an individual beneficial owner

        :param company_number : The company number of the individual beneficial owner details being requested..
        :param psc_id : The id of the individual beneficial owner details being requested.
        """

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.persons_with_significant_control,
            APIpaths.individual_beneficial_owner, psc_id)

        return response

    def get_corporate_entity_with_significant_control(self, company_number: str,
                                                      psc_id: str) -> requests.Response:
        """
        Get details of a corporate entity with significant control

        :param company_number : The company number of the corporate entity with significant control details being requested..
        :param psc_id : The id of the corporate entity with significant control details being requested.
        """

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.persons_with_significant_control,
            APIpaths.corporate_entity, psc_id)

        return response

    def get_corporate_entity_beneficial_owner(self, company_number: str,
                                              psc_id: str) -> requests.Response:
        """
        Get details of a corporate entity beneficial owner

        :param company_number : The company number of the corporate entity beneficial owner details being requested..
        :param psc_id : The id of the corporate entity beneficial owner details being requested.
        """

        response = self.__send_request(
            "GET", APIpaths.company, company_number,
            APIpaths.persons_with_significant_control,
            APIpaths.corporate_entity_beneficial_owner, psc_id)

        return response
