# Posio

Extracted from: https://github.com/abrenaut/posio.git

### Using Docker

Running root game:

docker run -e POSIO_SETTINGS=/app/config.py -p 8080:5000 \<Image>

Running feature flag:

docker run -e POSIO_SETTINGS=/app/config.py -e FEATURE_FLAG_FILE=/feature-flag/country -v \<Volume with feature flag file>:/feature-flag -p 8080:5000 \<Image>

## License

This project is under [MIT license](LICENSE).
