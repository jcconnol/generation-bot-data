CREATE TABLE IF NOT EXISTS poem_words (
	word text UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
	PRIMARY key(word)
);

CREATE TABLE IF NOT EXISTS poem_next_words (
	matching_word text NOT NULL,
	next_word text UNIQUE NOT NULL
);