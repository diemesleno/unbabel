GRANT ALL PRIVILEGES ON DATABASE unbabel TO unbabel;

CREATE TABLE IF NOT EXISTS public.translate (
    id integer NOT NULL,
    uid character varying(10) NOT NULL,
    original_text character varying(250) NOT NULL,
    translated_text character varying(250) NOT NULL,
    order_number integer,
    status character varying(20) NOT NULL,
    creation_date timestamp without time zone NOT NULL
);

ALTER TABLE public.translate OWNER TO unbabel;


CREATE SEQUENCE IF NOT EXISTS public.translate_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.translate_id_seq OWNER TO unbabel;

ALTER SEQUENCE public.translate_id_seq OWNED BY public.translate.id;

ALTER TABLE ONLY public.translate ALTER COLUMN id SET DEFAULT nextval('public.translate_id_seq'::regclass);

ALTER TABLE ONLY public.translate
    ADD CONSTRAINT translate_order_number_key UNIQUE (order_number);

ALTER TABLE ONLY public.translate
    ADD CONSTRAINT translate_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.translate
    ADD CONSTRAINT translate_uid_key UNIQUE (uid);

