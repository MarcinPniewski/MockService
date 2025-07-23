from flask import request, Response
import os
import mimetypes

RESPONSES_DIR = os.path.join(os.path.dirname(__file__), 'responses')

def find_existing_file(basename: str, extensions: list[str]) -> tuple[str, str] | None:
    for ext in extensions:
        filename = f"{basename}.{ext}"
        filepath = os.path.join(RESPONSES_DIR, filename)
        if os.path.isfile(filepath):
            return filepath, ext
    return None

def register_routes(app, logger):
    @app.route('/statusZadania', methods=['GET'])
    def status_zadania():
        kod = request.args.get('kod')

        if kod is None:
            logger.warning("400 BAD REQUEST — Brak parametru 'kod'")
            return Response("Brak parametru 'kod'", mimetype='text/plain'), 400

        # Typy obługiwanych plików
        preferred_extensions = ['txt', 'html', 'xml', 'json']

        result = find_existing_file(kod, preferred_extensions)

        if kod in ["zadanie_1", "zadanie_2"] and result:
            filepath, ext = result
            with open(filepath, 'r') as f:
                content = f.read()
                mimetype = mimetypes.types_map.get(f".{ext}", 'text/plain')
                logger.info(f"200 OK — Odpowiedź z pliku: {filepath}")
                return Response(content, mimetype=mimetype), 200

        else:
            fallback_result = find_existing_file("nieznane", preferred_extensions)
            if fallback_result:
                fallback_path, fallback_ext = fallback_result
                with open(fallback_path, 'r') as f:
                    content = f.read().replace("?kod=zadanie_3", f"?kod={kod}")
                    mimetype = mimetypes.types_map.get(f".{fallback_ext}", 'text/plain')
                    logger.info(f"400 BAD REQUEST — Odpowiedź z pliku: {fallback_path} dla kodu: {kod}")
                    return Response(content, mimetype=mimetype), 400
            else:
                logger.warning(f"Brak fallbackowego pliku nieznane.(txt/html/...) dla kodu: {kod}")
                return Response("Brak odpowiedzi", mimetype='text/plain'), 400