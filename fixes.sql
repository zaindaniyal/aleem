CREATE TABLE "android_metadata" ("locale" TEXT DEFAULT 'en_US');
INSERT INTO "android_metadata" VALUES ('en_US');

UPDATE khalifah_rabeh_ra SET chapter_id = (SELECT chapter_id FROM verses WHERE id = khalifah_rabeh_ra.id);
UPDATE khalifah_rabeh_ra SET verse_id = (SELECT verse_id FROM verses WHERE id = khalifah_rabeh_ra.id);

UPDATE tafsir_sagheer SET chapter_id = (SELECT chapter_id FROM verses WHERE id = tafsir_sagheer.id);
UPDATE tafsir_sagheer SET verse_id = (SELECT verse_id FROM verses WHERE id = tafsir_sagheer.id);

ALTER TABLE chapters ADD start INTEGER;
ALTER TABLE chapters ADD end INTEGER;
UPDATE chapters SET end = (SELECT id FROM (SELECT id, chapter_id, max(verse_id) FROM verses GROUP BY chapter_id) where chapter_id = chapters.chapter_id)
UPDATE chapters SET start = (SELECT MIN(id) FROM verses WHERE verses.chapter_id = chapters.chapter_id);