"""The geographic axis — where languages are.

A point is a crude proxy for an area, so the metric is trustworthy WITHIN a
dialect continuum and sceptical across macrolanguages. These tests assert the
former and document the latter.
"""
import orthography2ipa as o2i
from orthography2ipa import geographic_distance


def test_geography_recapitulates_the_iberian_continuum():
    """Independently of any linguistic data, the closest pair in the Iberian set
    is Mirandese and Asturian — which is precisely their genealogical
    relationship (Mirandese IS Astur-Leonese). Geography and genealogy agree
    without being told to."""
    def km(a, b):
        return geographic_distance(o2i.get(a), o2i.get(b), normalize=False)

    assert km("mwl", "ast") < km("mwl", "es-ES")
    assert km("gl", "ast") < km("gl", "es-ES")
    assert km("pt-PT", "gl") < km("pt-PT", "es-ES")


def test_distance_is_symmetric_and_self_zero():
    pt, gl = o2i.get("pt-PT"), o2i.get("gl")
    assert geographic_distance(pt, pt, normalize=False) == 0.0
    a = geographic_distance(pt, gl, normalize=False)
    b = geographic_distance(gl, pt, normalize=False)
    assert abs(a - b) < 1e-9


def test_absent_location_is_none_not_zero():
    """Two languages of unknown position are not thereby neighbours. Absence must
    not masquerade as proximity."""
    pt = o2i.get("pt-PT")
    unlocated = next(
        (o2i.get(c) for c in o2i.available_codes() if o2i.get(c).location is None),
        None)
    assert unlocated is not None, "expected at least one spec with no location"
    assert geographic_distance(pt, unlocated) is None


def test_normalisation_is_bounded():
    pt, ja = o2i.get("pt-PT"), o2i.get("ja")
    norm = geographic_distance(pt, ja)
    assert 0.0 <= norm <= 1.0


def test_locations_are_sourced_never_invented():
    """Every location says where it came from. A point with no provenance is a
    guess, and a guessed coordinate silently corrupts every comparison."""
    located = [o2i.get(c) for c in o2i.available_codes()
               if o2i.get(c).location is not None]
    assert located, "expected some specs to carry a location"
    for spec in located:
        assert spec.location.source, f"{spec.code}: location has no source"
        assert -90.0 <= spec.location.latitude <= 90.0
        assert -180.0 <= spec.location.longitude <= 180.0
