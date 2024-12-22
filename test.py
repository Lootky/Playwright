import requests
import pytest

def validate_get_pet(data):
    assert isinstance(data, dict), "Это не json"
    assert "id" in data and isinstance(data["id"], int), "ID не целое число"
    assert "category" in data and isinstance(data["category"], dict)

@pytest.mark.parametrize("status", ['pending', 'sold'])
def test_get_pet(status):
    url = f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}"
    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()
    if isinstance(data, list):
        assert len(data) > 0, "Response list is empty"
        for item in data:
            validate_get_pet(item)
    else:
        validate_get_pet(data)



def frame_text(text: str, weight: int, qwe: int) -> str:
    # Validate inputs
    if len(text) > weight - 4:
        raise ValueError("Text is too long for the given weight.")

    if qwe < 3:
        raise ValueError("qwe must be at least 3 to fit the text and borders.")

    # Create the top and bottom border
    border = "#" * weight

    # Calculate padding lines
    padding_lines = (qwe - 3) // 2

    # Create the empty line with padding
    padding = "#" + " " * (weight - 2) + "#"

    # Center the text with appropriate spaces
    text_line = text.center(weight - 2)
    text_line = f"#{text_line}#"

    # Build the full frame
    frame = [border] + [padding] * padding_lines + [text_line] + [padding] * (qwe - 3 - padding_lines) + [border]

    # Join all lines with a newline
    return "\n".join(frame)

# Example usage
result = frame_text("Hello, World!", 17, 7)
print(result)



def two_ten(q = int(input('Введи число: '))):
    if q < 0:
        print('внатуре? Отрицательное????')
    else:
        w = ''
        while q > 0:
            w = str(q % 2) + w
            q = q // 2
    return w
print(two_ten())