from companies_house.src.companies_house_api_client import CompaniesHouse

COC_NUMBER = '11799251'

ch = CompaniesHouse()


def test_get_companies_profile():
    response = ch.get_company_profile(COC_NUMBER)
    assert response.status_code == 200


def test_advanced_company_search():
    response = ch.advanced_company_search(company_name_includes='Swishfund')
    assert response.status_code == 200


def test_get_officers():
    response = ch.get_officers(COC_NUMBER)
    assert response.status_code == 200


def test_get_company_filing_history():
    response = ch.get_company_filing_history(COC_NUMBER)
    assert response.status_code == 200


def test_get_company_insolvency_information():
    response = ch.get_company_insolvency_information(COC_NUMBER)
    assert response.status_code == 200


def test_get_company_profile():
    response = ch.get_company_profile(COC_NUMBER)
    assert response.status_code == 200


def test_get_company_uk_enstablishment():
    response = ch.get_company_uk_enstablishment(COC_NUMBER)
    assert response.status_code == 200


def test_get_persons_with_significant_control():
    response = ch.get_persons_with_significant_control(COC_NUMBER)
    assert response.status_code == 200


def test_search_all():
    response = ch.search_all('Swishfund')
    assert response.status_code == 200


def test_search_companies():
    response = ch.search_companies('Swishfund')
    assert response.status_code == 200


def test_search_disqualified_officers():
    response = ch.search_disqualified_officers('Swishfund')
    assert response.status_code == 200


def test_search_officers():
    response = ch.search_officers('Swishfund')
    assert response.status_code == 200
