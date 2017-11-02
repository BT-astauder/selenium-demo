from robot.libraries.BuiltIn import BuiltIn

def output_video_url():
    session_id = BuiltIn().get_library_instance('Selenium2Library')._current_browser().session_id
    BuiltIn().log_to_console("VIDEO_URL: http://s3-eu-central-1.amazonaws.com/kc30ea1a-6y9b-a38c-1e64-t2u8d227g8a9/3554100e-6ddf-15c4-02e7-c1cad38c2da0/play.html?"+session_id)


