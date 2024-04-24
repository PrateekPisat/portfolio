"""Seed data.

Revision ID: 23a0934b516e
Revises: 055bb413e8ce
Create Date: 2023-03-04 13:42:10.650762

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "23a0934b516e"
down_revision = "055bb413e8ce"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO portfolio."group" (id, name, created_at, updated_at)
        VALUES (
                2,
                'Landscape',
                '2023-02-20 13:04:32.48581-05',
                NULL
            ),
            (
                3,
                'Portrait',
                '2023-02-20 13:04:32.48581-05',
                NULL
            ),
            (
                4,
                'Editorial',
                '2023-02-20 13:04:32.48581-05',
                NULL
            ),
            (
                5,
                'Still Life',
                '2023-02-20 13:04:32.48581-05',
                NULL
            );
        """
    )
    op.execute(
        """
        INSERT INTO portfolio."user" (
                id,
                username,
                "password",
                first_name,
                last_name,
                instagram_username,
                bio,
                "location",
                total_photos,
                created_at,
                updated_at,
                profile_picture_path,
                github_username,
                unsplash_username,
                email,
                about_picture_path
            )
        VALUES (
                1,
                'prateekpisat',
                'fake_pass',
                'Prateek',
                'Pisat',
                'prateekpisat',
                'Lauren''s unique photographic foundation is rooted with moody undertones and otherworldly terrains. Using creative set design and cinematic motifs, she forges a dream landscape for her subject matter. She is a visual creator with a strong base on human emotion and expressive storytelling.',
                'Boston, MA',
                0,
                '2023-02-05 13:04:46.028325-05',
                '2023-01-16 00:00:00-05',
                'thumbnails/profile_picture.jpeg',
                'PrateekPisat',
                'prateekpisat',
                'pisatprateek12@gmail',
                'thumbnails/about_picture.jpeg'
            );
        """
    )

    op.execute(
        """
    INSERT INTO portfolio.image (
		created_at,
		updated_at,
		width,
		height,
		blur_hash,
		description,
		city,
		country,
		full_path,
		thumbnail_path,
		group_id
	)
    VALUES (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            6000,
            3598,
            'LB8|khM}WUo2~VofNHt6s,t6WCkB',
            NULL,
            'Boston, MA',
            'United States',
            'full/Skyline.jpg',
            'thumbnails/Skyline.jpg',
            2
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            6000,
            4000,
            'L|HL;;ocoIWBPEWCofj[I^bIj[az',
            NULL,
            'Burlington, VA',
            'United States',
            'full/Trail-3.jpg',
            'thumbnails/Trail-3.jpg',
            2
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            6000,
            4000,
            'L9I#rzIUtS~q?ut7ofITxuofV@D%',
            NULL,
            'Boston, MA',
            'United States',
            'full/bird-4.jpg',
            'thumbnails/bird-4.jpg',
            3
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            3024,
            3780,
            'LpH2$mt7t7M{?wR*ofWAR%IUaet7',
            NULL,
            'Boston, MA',
            'United States',
            'full/cathedral.jpg',
            'thumbnails/cathedral.jpg',
            2
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            4000,
            6000,
            'L6Cr}x*|D*ADY*jE$jVsAKJ7xurX',
            NULL,
            'Burlington, VA',
            'United States',
            'full/lake-4-2.jpg',
            'thumbnails/lake-4-2.jpg',
            2
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            5199,
            3512,
            'L12P3.ay00t7offQWBj[00j[~qWB',
            NULL,
            'Boston, MA',
            'United States',
            'full/moon_3.jpg',
            'thumbnails/moon_3.jpg',
            2
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            6000,
            4000,
            'L~LD$EWBayay~qayj[ayRjjtj[a|',
            NULL,
            'Burlington, VA',
            'United States',
            'full/vermont-trail-2.jpg',
            'thumbnails/vermont-trail-2.jpg',
            2
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            6000,
            4000,
            'LwG9Egs,ofay0ga#ayj[s9WDWBay',
            NULL,
            'Boston, MA',
            'United States',
            'full/Bird.jpg',
            'thumbnails/Bird.jpg',
            3
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            6000,
            4000,
            'LKDJeY-.D%I:~VxuNGM_pIoMxYRQ',
            NULL,
            'Boston, MA',
            'United States',
            'full/Butterfly-5.jpg',
            'thumbnails/Butterfly-5.jpg',
            3
        );
    """
    )
    op.execute(
        """
        INSERT INTO portfolio.image (
            created_at,
            updated_at,
            width,
            height,
            blur_hash,
            description,
            city,
            country,
            full_path,
            thumbnail_path,
            group_id
        )
    VALUES (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            4914,
            4000,
            'LcGj~F=^v}R%0#Nxt7kCbINbX9WE',
            NULL,
            'Boston, MA',
            'United States',
            'full/Ganpati.jpg',
            'thumbnails/Ganpati.jpg',
            3
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            5444,
            3518,
            'LSF=R1~AoyE*SJ9axu-T-oWBoLWA',
            NULL,
            'Boston, MA',
            'United States',
            'full/Harshad_varadha.jpg',
            'thumbnails/Harshad_varadha.jpg',
            3
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            6000,
            4000,
            'LtG0Ost8s+aJ?bbdaeWE.AIoofkC',
            NULL,
            'Burlington, VA',
            'United States',
            'full/Lake.jpg',
            'thumbnails/Lake.jpg',
            2
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            6000,
            4000,
            'LtFZpZo#t3aJ?bXAaeWE.AM{off+',
            NULL,
            'Burlington, VA',
            'United States',
            'full/Lake_2.jpg',
            'thumbnails/Lake_2.jpg',
            2
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            6000,
            4000,
            'LSIzCW9bI:EN~9M|kCe.n$azofn~',
            NULL,
            'Burlington, VA',
            'United States',
            'full/Trail-5.jpg',
            'thumbnails/Trail-5.jpg',
            2
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            6000,
            4000,
            'LDBqCW_H049I9Zt6nPRpH]IUyBxt',
            NULL,
            'Boston, MA',
            'United States',
            'full/bird-2.jpg',
            'thumbnails/bird-2.jpg',
            3
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            6000,
            4000,
            'LEGuBb}xD+ImJ4O8J7kWA8OQWBkD',
            NULL,
            'Boston, MA',
            'United States',
            'full/bird-3.jpg',
            'thumbnails/bird-3.jpg',
            3
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            6000,
            4000,
            'LYC?DroLayae0KWVayfkx]a|ofj[',
            NULL,
            'Boston, MA',
            'United States',
            'full/color_splash_bridge.jpg',
            'thumbnails/color_splash_bridge.jpg',
            2
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            6000,
            4000,
            'LJCG*RXS0~v~x[V]ocWU0~nO:;OX',
            NULL,
            'Boston, MA',
            'United States',
            'full/flower-1.jpg',
            'thumbnails/flower-1.jpg',
            3
        );
        """
    )
    op.execute(
        """
        INSERT INTO portfolio.image (
            created_at,
            updated_at,
            width,
            height,
            blur_hash,
            description,
            city,
            country,
            full_path,
            thumbnail_path,
            group_id
        )
    VALUES (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            6000,
            4000,
            'LJCZU+H?9}k6t8NENMt10fx[+~%1',
            NULL,
            'Boston, MA',
            'United States',
            'full/flower-2.jpg',
            'thumbnails/flower-2.jpg',
            3
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            6000,
            4000,
            'LAEoxk0L4okO~VNNnN$]NXtRi%xa',
            NULL,
            'Boston, MA',
            'United States',
            'full/flower-3.jpg',
            'thumbnails/flower-3.jpg',
            3
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            6000,
            4000,
            'L86HcXS00x-BE2r@%2NH9=o3=hS0',
            NULL,
            'Boston, MA',
            'United States',
            'full/flower-4.jpg',
            'thumbnails/flower-4.jpg',
            3
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            6000,
            3375,
            'LGAKQlV]D+j?8%kBtOazb;kBjcay',
            NULL,
            'Boston, MA',
            'United States',
            'full/flower-5.jpg',
            'thumbnails/flower-5.jpg',
            3
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            4000,
            6000,
            'LSH.4v?vDiMw~pxaxaWB?b%LtRSi',
            NULL,
            'Boston, MA',
            'United States',
            'full/incense stick.jpg',
            'thumbnails/incense stick.jpg',
            3
        ),
        (
            '2023-03-02 14:34:47.116965-05',
            NULL,
            6000,
            4000,
            'L4C~bP[u0OLKPRr=E19]0|-\:o}Iq',
            NULL,
            'Burlington, VA',
            'United States',
            'full/lake-5.jpg',
            'thumbnails/lake-5.jpg',
            2
        );
    """
    )
    op.execute(
        """
        INSERT INTO portfolio.image (
            created_at,
            updated_at,
            width,
            height,
            blur_hash,
            description,
            city,
            country,
            full_path,
            thumbnail_path,
            group_id
        )
        VALUES (
                '2023-03-02 14:34:47.116965-05',
                NULL,
                4000,
                5455,
                'LZJao}Inoyoz0KR*spj@%MofRjRj',
                NULL,
                'Boston, MA',
                'United States',
                'full/plant.jpg',
                'thumbnails/plant.jpg',
                5
            ),
            (
                '2023-03-02 14:34:47.116965-05',
                NULL,
                6000,
                4000,
                'LC8gmIa$4pt7~oj]D*ofNHt6xuRk',
                NULL,
                'Boston, MA',
                'United States',
                'full/prateek-pisat-IhtPrpWbUBY-unsplash.jpg',
                'thumbnails/prateek-pisat-IhtPrpWbUBY-unsplash.jpg',
                2
            ),
            (
                '2023-03-02 14:34:47.116965-05',
                NULL,
                5555,
                4000,
                'LR9*=iRNRikD+pNHR%s+,9XUt3oJ',
                NULL,
                'Boston, MA',
                'United States',
                'full/skipping_rocks-2.jpg',
                'thumbnails/skipping_rocks-2.jpg',
                2
            ),
            (
                '2023-03-02 14:34:47.116965-05',
                NULL,
                4032,
                3024,
                'LTD]oD9aRha#?wWVofaeks%2M{t6',
                NULL,
                'Boston, MA',
                'United States',
                'full/skyline-1.jpg',
                'thumbnails/skyline-1.jpg',
                2
            ),
            (
                '2023-03-02 14:34:47.116965-05',
                NULL,
                3024,
                4032,
                'LwFQ8wWCofRj.AadfkayXUt7afof',
                NULL,
                'Boston, MA',
                'United States',
                'full/skyline-2.jpg',
                'thumbnails/skyline-2.jpg',
                2
            ),
            (
                '2023-03-02 14:34:47.116965-05',
                NULL,
                6000,
                4000,
                'LgJGlw=_Ios,0gR*%KS3IrNIWCod',
                NULL,
                'Boston, MA',
                'United States',
                'full/steps.jpg',
                'thumbnails/steps.jpg',
                2
            ),
            (
                '2023-03-02 14:34:47.116965-05',
                NULL,
                6000,
                4000,
                'LcGIcd?bRijYKTIuocofpfo$WCa$',
                NULL,
                'Boston, MA',
                'United States',
                'full/stones.jpg',
                'thumbnails/stones.jpg',
                2
            ),
            (
                '2023-03-02 14:34:47.116965-05',
                NULL,
                6000,
                4000,
                'L99s^;xv4=%11RSP$~f+9b-U-may',
                NULL,
                'Boston, MA',
                'United States',
                'full/trail-14.jpg',
                'thumbnails/trail-14.jpg',
                2
            ),
            (
                '2023-03-02 14:34:47.116965-05',
                NULL,
                6000,
                4000,
                'L~J*oBj[WBaz~qj[ayfQRjayf7fQ',
                NULL,
                'Burlington, VA',
                'United States',
                'full/vermont-trail-1.jpg',
                'thumbnails/vermont-trail-1.jpg',
                2
            ),
            (
                '2023-03-02 14:34:47.116965-05',
                NULL,
                4000,
                6000,
                'LBJsXY}k0.V@s,xZs:Rm^HNLi_of',
                NULL,
                'Burlington, VA',
                'United States',
                'full/vermont-trail-3.jpg',
                'thumbnails/vermont-trail-3.jpg',
                2
            );
        """
    )


def downgrade() -> None:
    op.execute("TRUNCATE TABLE portfolio.image;")
    op.execute("TRUNCATE TABLE portfolio.user;")
    op.execute("TRUNCATE TABLE portfolio.group cascade;")
