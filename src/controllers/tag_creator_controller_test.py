from src.controllers.tag_creator_controller import TagCreatorController

def test_create():
    mock_value = "image_path"
    tag_creator_controller = TagCreatorController()

    result = tag_creator_controller.create(mock_value)

    assert isinstance(result, dict)
    assert "data" in result
    assert "path" in result["data"]
