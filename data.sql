--
-- PostgreSQL database dump
--

\restrict tVjJ1dx8Xu75yQHffI0Svbs3ziFdcrec6NY2X9ktSN7pTCsufQHmEqxeDUw5tFn

-- Dumped from database version 18.6
-- Dumped by pg_dump version 18.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: sallomone
--

INSERT INTO public.users (id, username, password_hash, is_writer) VALUES (1, 'a', 'scrypt:32768:8:1$U5X3htXYnjJSu6SA$3a3c763f53dab886f41041592b64a50d525b50ece0ca929913ccb674062f794525f43f2acff74bce87d37b8db547221d56133a005d5ddd1e83f2c107e2ad1915', true);
INSERT INTO public.users (id, username, password_hash, is_writer) VALUES (2, 'Professor', 'scrypt:32768:8:1$J4IYRaeYtTrFrfLX$384adfca99a32b166d0c920a5dc437c45a4f92e8fd33de3883e788b192b7f9e6e7504a33be9f3ceab710ffa87997a7eb051a299906c94ba6d4a75c7c7b29e47c', true);
INSERT INTO public.users (id, username, password_hash, is_writer) VALUES (3, 'Demirhan', 'scrypt:32768:8:1$czAQG4GlHtrze7KA$d310cb73a5cef978c0e0db2ec34ec7cb6ab529d6e6918a278f0682ac8ff3c5e3640bdc39006585d01369aafaefe89be5e06d06001eab7b2349e5fb57846401cc', false);


--
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: sallomone
--

INSERT INTO public.posts (id, title, body, author_id, created_at) VALUES (1, 'first post', 'wow', 1, '2026-10-30 02:58:18.554719+01');
INSERT INTO public.posts (id, title, body, author_id, created_at) VALUES (2, 'How roles work', 'for now I update it manually by the database as i am writing this but i also have to see how the database translates to github as I have never done it before [=_=]', 2, '2026-10-30 03:03:35.978477+01');


--
-- Name: posts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sallomone
--

SELECT pg_catalog.setval('public.posts_id_seq', 2, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sallomone
--

SELECT pg_catalog.setval('public.users_id_seq', 3, true);


--
-- PostgreSQL database dump complete
--

\unrestrict tVjJ1dx8Xu75yQHffI0Svbs3ziFdcrec6NY2X9ktSN7pTCsufQHmEqxeDUw5tFn

